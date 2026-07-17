# Project Architecture

The Competitive Intelligence & Pricing Strategy Engine follows a modular architecture.

## Data Collection

- Amazon
- Flipkart
- Croma

Data is collected using:

- Playwright
- BeautifulSoup

---

## Data Processing

Collected data undergoes:

- Missing Value Handling
- Price Normalization
- Rating Normalization
- Discount Analysis

---

## Analytics Layer

The analytics engine performs:

- Competitor Segmentation
- Pricing Gap Analysis
- Opportunity Detection
- Elasticity Proxy

---

## Decision Engine

Business rules generate:

- Pricing Recommendations
- Strategic Recommendations
- Opportunity Scores
- Priority Products

---

## Presentation Layer

The processed data is visualized using:

- Streamlit
- Plotly
- Folium

Dashboards include:

- Executive Dashboard
- Pricing Simulator
- Competitor Monitor
- Geo Dashboard
- Export Center

---

## Deployment Layer

Application Deployment:

Docker

↓

Docker Compose

↓

Kubernetes

---

## Outcome

A complete Competitive Intelligence Platform capable of supporting strategic pricing decisions.