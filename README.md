# Heart Disease Prediction — End-to-End ML Deployment

A cardiovascular-risk classifier trained on Kaggle data, served through a Streamlit
interface, containerised with Docker and deployed on AWS EC2.

**Model:** LightGBM · **Validation:** 0.948 ROC AUC on the Kaggle leaderboard
([notebook](https://www.kaggle.com/code/karuna2k/heart-disease-prediction-ml-lightgbm-s6e2))

> ⚠️ This is a learning/portfolio project, **not** a medical device. It must not be used
> for real clinical decisions.

## What it does

Given 13 clinical parameters (age, sex, chest-pain type, resting BP, cholesterol, fasting
blood sugar, rest ECG, max heart rate, exercise-induced angina, ST depression, slope,
number of major vessels, thalassemia) the app returns a calibrated probability of heart
disease and a low / moderate / high risk band.

## Stack

| Layer | Tool |
|---|---|
| Model | LightGBM (scikit-learn API), serialised to `heart_model.pkl` |
| App | Streamlit (`app.py`) |
| Packaging | Docker |
| Hosting | AWS EC2 (Amazon Linux 2023) |

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py          # http://localhost:8501
```

## Run with Docker

```bash
docker build -t heart-app .
docker run -d -p 8501:8501 heart-app
```

A prebuilt image is published to Docker Hub:

```bash
docker pull karuna18/heart-app:latest
docker run -d -p 8501:8501 --restart unless-stopped karuna18/heart-app:latest
```

## Deployment notes (AWS EC2)

The container was pulled from Docker Hub onto an EC2 instance and run on port 8501.
Reaching it required opening the port in the instance Security Group — a reminder that
deployment is as much networking as modelling.

For a real deployment, terminate HTTPS at an Nginx/ALB reverse proxy and restrict the
Security Group to known sources rather than exposing the app port directly.

## Repository layout

```
app.py             Streamlit UI + inference
heart_model.pkl    trained LightGBM model
requirements.txt   Python dependencies
Dockerfile         container build
```

## Roadmap

- GitHub Actions: build + push image on every commit
- Nginx reverse proxy with HTTPS
- Input validation and model-version pinning
