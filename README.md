# Competitive Intelligence & Pricing Strategy Engine for E-Commerce

## Project Overview

This project is a complete Competitive Intelligence and Pricing Strategy Engine developed as part of the Aarivya Labs Data Analyst Internship Program.

The system collects competitor pricing data from multiple e-commerce platforms, cleans and analyzes the data, generates pricing recommendations, and visualizes strategic insights using an interactive Streamlit dashboard.

---

## Features

- Multi-platform competitor price scraping
- Data cleaning and normalization
- Competitor segmentation
- Pricing recommendation engine
- Executive analytics dashboard
- Geographic visualization
- Export reports (CSV & Excel)
- Docker containerization
- Kubernetes deployment configuration

---

## Technology Stack

### Programming

- Python 3.12

### Data Analysis

- Pandas
- NumPy
- Scikit-learn
- Statsmodels

### Web Scraping

- Playwright
- BeautifulSoup
- Requests

### Visualization

- Streamlit
- Plotly
- Folium

### Deployment

- Docker
- Docker Compose
- Kubernetes

---

## Project Structure

```
Project/
│
├── Week1/
├── Week2/
├── Week3/
├── Week4/
├── Week5/
├── Week6/
├── Week7/
│
├── deployment/
│   ├── docker/
│   └── kubernetes/
│
├── reports/
├── screenshots/
├── visuals/
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/SrijoMag/Competative-intelligence.git
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Dashboard

```bash
python -m streamlit run Week7/analysis/app.py
```

---

## Docker

Build

```bash
docker build -t competitive-pricing-engine -f deployment/docker/Dockerfile .
```

Run

```bash
docker run -p 8501:8501 competitive-pricing-engine
```

---

## Docker Compose

```bash
docker compose -f deployment/docker/docker-compose.yml up
```

---

## Kubernetes

```bash
kubectl apply -f deployment/kubernetes/configmap.yaml
kubectl apply -f deployment/kubernetes/deployment.yaml
kubectl apply -f deployment/kubernetes/service.yaml
```

---

## Dashboard Modules

- Executive Dashboard
- Pricing Analysis
- Competitor Segmentation
- Geographic Dashboard
- Strategic Recommendations
- Export Reports

---

## Screenshots

(Add screenshots here)

---

## Future Enhancements

- AI-powered pricing prediction
- Live competitor monitoring
- Email alerts
- Cloud deployment
- Automated report generation

---

## Author

**Srijoswin Mazumder**

Data Analyst Intern

Aarivya Labs

GitHub:
https://github.com/SrijoMag

LinkedIn:
(Add your LinkedIn profile)

---

## License

This project is developed for educational and internship purposes.