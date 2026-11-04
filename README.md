# Heart Disease Prediction — End-to-End ML Deployment

I built a cardiovascular-risk classifier, wrapped it in a Streamlit interface,
containerised it with Docker and deployed it on AWS EC2 — taking a model all the way
from a Kaggle notebook to a running public service.

**Model:** LightGBM · **Validation:** 0.948 ROC AUC on the Kaggle leaderboard
([my notebook](https://www.kaggle.com/code/karuna2k/heart-disease-prediction-ml-lightgbm-s6e2))

> ⚠️ I built this as a learning/portfolio project, **not** a medical device. It must not
> be used for real clinical decisions.

## What it does

I take 13 clinical parameters (age, sex, chest-pain type, resting BP, cholesterol, fasting
blood sugar, rest ECG, max heart rate, exercise-induced angina, ST depression, slope,
number of major vessels, thalassemia) and return a probability of heart disease along with
a low / moderate / high risk band.

## Stack

| Layer | Tool |
|---|---|
| Model | LightGBM (scikit-learn API), serialised to `heart_model.pkl` |
| App | Streamlit (`app.py`) |
| Packaging | Docker |
| Hosting | AWS EC2 (Amazon Linux 2023) |

## Run it locally

```bash
pip install -r requirements.txt
streamlit run app.py          # http://localhost:8501
```

## Run it with Docker

```bash
docker build -t heart-app .
docker run -d -p 8501:8501 heart-app
```

I also published a prebuilt image to Docker Hub:

```bash
docker pull karuna18/heart-app:latest
docker run -d -p 8501:8501 --restart unless-stopped karuna18/heart-app:latest
```

## How I deployed it (AWS EC2)

I pulled the image from Docker Hub onto an EC2 instance and ran it on port 8501. Getting it
reachable meant opening the port in the instance Security Group — a good reminder that
deployment is as much networking as modelling.

If I were to run this for real, I'd terminate HTTPS at an Nginx/ALB reverse proxy and
restrict the Security Group to known sources rather than exposing the app port directly.

## Repository layout

```
app.py             Streamlit UI + inference
heart_model.pkl    trained LightGBM model
requirements.txt   Python dependencies
Dockerfile         container build
```

## What I'd add next

- GitHub Actions to build + push the image on every commit
- Nginx reverse proxy with HTTPS
- Input validation and model-version pinning
