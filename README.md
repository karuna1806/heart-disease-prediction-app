❤️ Heart Disease Prediction
End-to-End Machine Learning Deployment on AWS using Docker


📌 1. Executive Summary

This project demonstrates a complete machine learning production workflow from raw dataset exploration to public cloud deployment.

The objective was not just to build a predictive model, but to:

Develop a usable web interface

Containerize the application

Deploy it on cloud infrastructure

Debug real-world networking issues

Make it publicly accessible

The final system is a live ML application deployed on AWS EC2, running inside a Docker container, accessible via public IP.

This project bridges the gap between:

Kaggle notebook → Production-grade deployment

🎯 2. Problem Statement

Cardiovascular diseases are one of the leading causes of mortality worldwide.
Early detection significantly improves survival rates.

The goal of this project is to:

Predict the likelihood of heart disease

Based on patient clinical parameters

Provide real-time predictions via a web interface

This system simulates a decision-support tool for medical screening.

📊 3. Dataset

Source: Kaggle Heart Disease Dataset "https://www.kaggle.com/code/karuna2k/heart-disease-prediction-ml-lightgbm-s6e2/edit"

Features Used:

Age

Sex

Chest Pain Type

Resting Blood Pressure

Cholesterol

Fasting Blood Sugar

Rest ECG

Max Heart Rate

Exercise Induced Angina

ST Depression

Slope

Number of Major Vessels

Thalassemia

Target:

0 → No Heart Disease

1 → Heart Disease Present

Data Preparation Steps:

Checked missing values

Verified data types

Basic distribution analysis

Train-test split

Feature scaling (if applied)

Encoded categorical features

📈 4. Exploratory Data Analysis (EDA)

EDA focused on:

Distribution of heart disease cases

Correlation between features and target

Age impact analysis

Chest pain type importance

Cholesterol patterns

Key insights:

Age shows positive correlation with disease risk.

Chest pain type strongly influences outcome.

Certain categorical variables significantly affect prediction.

EDA ensured data understanding before modeling.

🤖 5. Model Development
Algorithm Used:

(Logistic Regression / Random Forest / Light GBM etc.)

Why This Model?

Balanced bias-variance tradeoff

Good performance on tabular medical data

Interpretable (if logistic regression)

Training Steps:

Train-test split (80/20)

Model training

Performance evaluation

Metrics:

Accuracy

Precision

Recall

F1-score

Overfitting was evaluated by comparing train and test performance.

💾 6. Model Serialization

The trained model was saved using:

pickle.dump(model, open("heart_model.pkl", "wb"))

Why?

Allows model reuse without retraining

Enables integration into web applications

Essential for deployment

🌐 7. Web Application – Streamlit

An interactive frontend was built using Streamlit.

Features:

Slider inputs (Age, Cholesterol, BP)

Dropdown selections (Sex, Chest Pain)

Real-time prediction button

Clean UI layout

Prediction flow:

User enters parameters

Data is formatted

Model .pkl loaded

Prediction returned

Result displayed instantly

This converts ML into a usable product.

🐳 8. Containerization using Docker

To ensure consistent environment execution, the app was containerized.

Why Docker?

Environment consistency

Portability

Production readiness

Easy cloud deployment

Dockerfile Includes:

Python base image

Requirements installation

App copy

Port exposure (8501)

Streamlit run command

Build Command:
docker build -t heart-app .
Run Command:
docker run -d -p 8501:8501 heart-app
☁️ 9. DockerHub Integration

The image was tagged and pushed to DockerHub:

docker tag heart-app karuna18/heart-app:latest
docker push karuna18/heart-app:latest

Purpose:

Public image hosting

Cloud deployment compatibility

CI/CD readiness

🖥 10. AWS EC2 Deployment
Infrastructure Setup:

Launched EC2 (Amazon Linux 2023)

Configured key pair (PEM)

SSH connection established

Installed Docker manually

Pulled image from DockerHub

docker pull karuna18/heart-app:latest
Container Execution:
docker run -d -p 8501:8501 --restart unless-stopped karuna18/heart-app:latest
🔐 11. Networking & Security Configuration

One of the major real-world challenges encountered:

"Site can’t be reached"

Root cause:

Port 8501 not allowed in Security Group.

Fix:

Edited EC2 Security Group

Added inbound rule:

Custom TCP

Port 8501

Source: 0.0.0.0/0

After update:

Application accessible via public IP

Verified using:

docker ps

netstat

curl ifconfig.me

This debugging phase provided hands-on cloud networking experience.

🧠 12. Infrastructure Lessons Learned

This project provided exposure to:

Cloud security groups

Public IP management

Docker networking

SSH authentication

Restart policies

Firewall configuration

Realizations:

Deployment ≠ Model training

Infrastructure knowledge is critical

Debugging is part of engineering

🔄 13. CI/CD (Future Improvement Plan)

Planned enhancements:

GitHub Actions workflow

Automatic Docker build on push

Automatic image push to DockerHub

EC2 auto deployment

Nginx reverse proxy

HTTPS with SSL

Elastic IP configuration

Load balancer

ECS migration

This would convert the project into full production-grade architecture.

🏗 14. System Architecture

User
↓
Public IP (EC2)
↓
Docker Container
↓
Streamlit Application
↓
Loaded ML Model (.pkl)
↓
Prediction Output

📸 15. Final Output

Publicly accessible Streamlit app

Docker container running on AWS

Fully functional ML web application

This demonstrates:

Machine Learning

Application development

Containerization

Cloud deployment

Infrastructure debugging

💼 16.Summary

Heart Disease Prediction – End-to-End ML Deployment (AWS + Docker)

Built and evaluated ML model for cardiovascular risk prediction

Developed interactive Streamlit web application

Containerized application using Docker

Pushed image to DockerHub

Deployed container on AWS EC2

Configured security groups and public networking

Implemented restart policies for resilience

🔥 17. Personal Reflection

This project represents a transition:

From:
Notebook-based ML experimentation

To:
Production-oriented ML engineering

It demonstrates the ability to:

Build models

Package applications

Deploy infrastructure

Debug networking

Operate cloud systems

This is not just a Kaggle project.

It is an end-to-end ML deployment system.
![WhatsApp Image 2026-02-27 at 04 44 10](https://github.com/user-attachments/assets/1d5aa5fd-074d-4241-b74e-7e633e0332a1)
![WhatsApp Image 2026-02-27 at 04 44 101](https://github.com/user-attachments/assets/411d2d6d-539d-4475-8b4e-369b6417325a)

Live URL link "http://100.31.188.39:8501" It might not be running after some times when I stops EC2 server from AWS.
