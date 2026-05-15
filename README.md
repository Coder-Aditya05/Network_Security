# 🔐 Network Security — Phishing Detection System

An end-to-end Machine Learning project for detecting phishing activity in network traffic. Built with a modular MLOps pipeline, REST API for real-time predictions, and experiment tracking via MLflow and DagsHub.

---

## 📌 Overview

Phishing attacks are one of the most common cybersecurity threats. This project uses machine learning to classify network traffic data as **phishing or legitimate**, deployed as a production-ready web application.

---

## 🏗️ Project Architecture

```
Network_Security/
├── Network_Security/
│   ├── components/          # Data ingestion, validation, transformation, model trainer
│   ├── pipeline/            # Training pipeline
│   ├── entity/              # Config and artifact entities
│   ├── utils/               # Utility functions
│   ├── constant/            # Project constants
│   ├── exception/           # Custom exception handling
│   └── logging/             # Custom logger
├── Network_Data/            # Raw network dataset
├── final_model/             # Saved model & preprocessor
├── prediction_output/       # CSV output of predictions
├── templates/               # HTML templates (Jinja2)
├── app.py                   # FastAPI application
├── main.py                  # Training pipeline runner
├── Dockerfile               # Docker configuration
└── requirements.txt
```

---

## ⚙️ ML Pipeline

The pipeline runs sequentially through the following stages:

1. **Data Ingestion** — Pulls data from MongoDB Atlas into train/test splits
2. **Data Validation** — Validates schema and checks for data drift
3. **Data Transformation** — Applies preprocessing (scaling, encoding, imputation)
4. **Model Training** — Trains a classifier and evaluates performance metrics

---

## 🚀 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET`  | `/`      | Redirects to API docs |
| `GET`  | `/train` | Triggers the full training pipeline |
| `POST` | `/predict` | Upload a CSV file and get predictions |

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.12 |
| ML | scikit-learn, pandas, NumPy |
| API | FastAPI, Uvicorn |
| Database | MongoDB Atlas (pymongo) |
| Experiment Tracking | MLflow, DagsHub |
| Containerization | Docker, AWS CLI |
| CI/CD | GitHub Actions |

---

## 🔧 Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/Coder-Aditya05/Network_Security.git
cd Network_Security
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the root directory:
```
MONGO_DB_URL=your_mongodb_connection_string
```

### 5. Run the application
```bash
python app.py
```

Visit `http://localhost:8000/docs` for the interactive API documentation.

---

## 🏋️ Train the Model

Trigger training via the API:
```
GET http://localhost:8000/train
```

Or run the training pipeline directly:
```bash
python main.py
```

---

## 📊 Predict on New Data

Send a POST request to `/predict` with a CSV file. The API returns an HTML table with a `Predicted_Column` appended, and saves results to `prediction_output/output.csv`.

---

## 🐳 Run with Docker

```bash
docker build -t network-security .
docker run -p 8000:8000 network-security
```

---

## 📈 Experiment Tracking

Model experiments are tracked using **MLflow** integrated with **DagsHub**. Each training run logs metrics, parameters, and model artifacts for comparison and reproducibility.

---

## 📬 Contact

**Aditya** — [GitHub](https://github.com/Coder-Aditya05)
