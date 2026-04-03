import uuid
from pathlib import Path
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS

from services.storage import ensure_case_dirs, get_case_dir
from services.ct_input import save_single_ct_from_upload
from services.inference import run_ct_ich_inference, generate_ct_previews, mask_to_mesh


BASE_DIR = Path(__file__).resolve().parent
CASES_DIR = BASE_DIR / "cases"

app = Flask(__name__)
CORS(app)

@app.get("/api/health")
def health():
    return jsonify({"status": "ok"})

@app.post("/api/ct-spleen/submit")
def ct_ich_submit():
    if "file" not in request.files:
        return jsonify({"error": "No file field named 'file'"}), 400

    f = request.files["file"]
    filename = (f.filename or "").lower()

    if not (filename.endswith(".nii") or filename.endswith(".nii.gz") or filename.endswith(".zip")):
        return jsonify({"error": "Upload must be .nii, .nii.gz, or .zip"}), 400

    workflow = "ct-spleen"
    case_id = str(uuid.uuid4())
    case_dir = ensure_case_dirs(CASES_DIR, workflow, case_id)

    # save the raw upload
    suffix = ".zip" if filename.endswith(".zip") else (".nii.gz" if filename.endswith(".nii.gz") else ".nii")
    upload_path = case_dir["input"] / f"upload{suffix}"
    f.save(upload_path)

    def file_url(relpath: str) -> str:
            return f"/api/case/{workflow}/{case_id}/download/{relpath}"

    # validate/extract -> standardized ct.nii(.gz)
    try:
        ct_path = save_single_ct_from_upload(upload_path, case_dir["input"])
        mask_path = case_dir["output"] / "mask.nii.gz"
        run_ct_ich_inference(ct_path, mask_path)
        previews = generate_ct_previews(ct_path, case_dir["preview"], n_slices=24)
        mesh_path = case_dir["mesh"] / "mask.ply"
        mask_to_mesh(mask_path, mesh_path)

        preview_urls = {
            plane: [file_url(f"output/preview/{fn}") for fn in files]
            for plane, files in previews.items()
        }
    except Exception as e:
        return jsonify({"error": f"Input validation failed: {e}"}), 400

    return jsonify({
        "workflow": workflow,
        "case_id": case_id,
        "message": "Upload OK. CT saved. Inference + assets generated.",
        "outputs": {
            "ct_url": file_url(ct_path.relative_to(case_dir["case"]).as_posix()),
            "mask_url": file_url(mask_path.relative_to(case_dir["case"]).as_posix()),
            "mesh_url": file_url(mesh_path.relative_to(case_dir["case"]).as_posix()),
            "previews": preview_urls,
        }
    })

@app.get("/api/case/<workflow>/<case_id>/download/<path:relpath>")
def download_case_file(workflow: str, case_id: str, relpath: str):
    case_dir = get_case_dir(CASES_DIR, workflow, case_id)
    target = case_dir / relpath
    if not target.exists():
        return jsonify({"error": "file not found"}), 404
    try:
        target.relative_to(case_dir)
    except ValueError:
        return jsonify({"error": "invalid path"}), 400
    return send_from_directory(target.parent, target.name, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
