
# 🚀 ML Web App — Streamlit + Docker

An interactive **Machine Learning Web Application** built with **Streamlit** and containerized using **Docker**.  
This project demonstrates how to train a model, deploy it as a simple web interface, and make it portable for anyone to run — anywhere, anytime. 🧠✨

---

## 🧩 Table of Contents
- [Overview](#-overview)
- [Project Structure](#-project-structure)
- [Features](#-features)
- [Setup & Run (Docker)](#-setup--run-docker)
- [Run Locally (Without Docker)](#-run-locally-without-docker)
- [Dockerfile Explained](#-dockerfile-explained)
- [Collaboration Guide](#-collaboration-guide)
- [Future Improvements](#-future-improvements)
- [Author](#-author)
- [Support](#-support)

---

## 🌍 Overview

This project showcases an **end-to-end ML pipeline**:
- Train a model with `train_model.py`
- Save it as `model.pkl`
- Load and visualize predictions in `app_streamlit.py`
- Package the entire app into a **Docker container**

The container ensures your app runs **exactly the same** on any machine —  
no dependency conflicts, no setup headaches. 🐳💻

---

## 📂 Project Structure

```bash
mlapp/
├── app.py                # Optional main script
├── app_streamlit.py      # Streamlit web interface
├── train_model.py        # ML model training script
├── model.pkl             # Saved trained model
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
└── __pycache__/          # Cache folder (ignored)
```
## 🐳 Run with Docker

To build, run, and open the app in one go:


# 1️⃣ Build the image
```bash
docker build -t mlapp .
```
# 2️⃣ Run the container
```bash
docker run -p 8501:8501 mlapp
```

# 3️⃣ Open the app in your browser
```bash
# (Once container starts, visit)
# 👉 http://localhost:8501
```

