<img width="254" height="62" alt="image" src="https://github.com/user-attachments/assets/8a623310-0bcf-492b-8727-f3352268b8e9" /># Hospital-Management-system-and-PACS-system
An end-to-end, production-oriented PACS system that integrates automated medical image segmentation, interactive 2D/3D visualization, and AI-assisted clinical workflows. The platform supports DICOM/NIfTI/NRRD data ingestion, GPU-accelerated deep learning inference (nnU-Net/U-Net) for lung, brain, and spleen segmentation, and real-time 3D rendering in the browser. Built with a microservice architecture (Spring Boot, Python Flask, Vue.js, Docker), it also includes RAG-based AI chatbots for patients and clinicians, secure role-based access control, and hospital-grade deployment components (Orthanc, MinIO, MySQL).

## 🚀 Key Features

- **Hospital Management System**
  - User authentication and role-based access
  - Patient, doctor, and appointment management
  - Secure clinical data handling
  - **Fine-tuned role-based AI chatbot** for different user roles (e.g., doctors, radiologists, patients) to support clinical queries and system interaction
  - Chatbot: <img width="458" height="520" alt="image" src="https://github.com/user-attachments/assets/7de3fb99-c1b5-4d3d-9836-e9daf3b062f5" />


- **PACS System**
  - DICOM/NIfTI/NRRD medical image support
  - Automated AI-based segmentation (CT/MRI)
  - Interactive 2D/3D medical image visualization
  - Real-time processing pipeline
  - **AI segmentation page: <img width="968" height="585" alt="image" src="https://github.com/user-attachments/assets/47aafc4c-ec2c-4b02-b24e-1d180b27214a" />
  - **2D/3D medical image visualization   <img width="975" height="472" alt="image" src="https://github.com/user-attachments/assets/3c689665-7085-4cfe-a691-42d7c5d88dec" />
  - **Brain MRI: <img width="975" height="986" alt="image" src="https://github.com/user-attachments/assets/1f2d3f4c-fc09-4dd4-9b28-41b0580cd268" />

  



- **AI Capabilities**
  - Deep learning–based medical image segmentation (nnU-Net / U-Net)
  - Python-based inference services
  - Modular design for extending AI models
  - <img width="986" height="1060" alt="image" src="https://github.com/user-attachments/assets/75f9c80d-4564-4432-b52f-65da17d2eb89" />

  - <img width="1019" height="336" alt="image" src="https://github.com/user-attachments/assets/a98be3e6-f1ad-4063-835b-f8a54770bb6e" />


---

## 🏗️ System Architecture

- **Frontend**: Web-based UI for hospital and PACS operations  
- **Backend (Java)**: Spring Boot services for business logic and APIs  
- **Backend (Python)**: Flask-based AI inference and image processing services  
- **Database**: MySQL for structured hospital data  
- **Deployment**: Docker-ready microservice architecture  

---

## 🛠️ Tech Stack

- **Frontend**: Vue.js / Web UI
- **Backend (Java)**: Spring Boot, MyBatis
- **Backend (Python)**: Flask, PyTorch
- **AI Models**: nnU-Net, U-Net, TotalSegmentator

- **Database**: MySQL
- **Medical Imaging**: DICOM, NIfTI, NRRD
- **Tools**: Docker, Git, IntelliJ IDEA

---
