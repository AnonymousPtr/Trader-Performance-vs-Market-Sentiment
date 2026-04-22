# Trader Behavior vs Market Sentiment

## Overview
This project analyzes how Bitcoin market sentiment (Fear vs Greed) influences trader behavior and performance using Hyperliquid trading data. The analysis focuses on behavioral patterns, risk exposure, and performance variation across different sentiment regimes.
Due to limited temporal coverage, the study is conducted as a cross-sectional analysis, emphasizing differences in trader behavior rather than time-series trends.

---

## Live Dashboard
Streamlit App:  
https://trader-performance-vs-market-sentiment-ggjkgrfrxpdjmd7yvuzyjh.streamlit.app/

---

## Repository Structure

```
ASSESSMENT/
│
├── Datasets/
│   ├── fear_greed_index.csv
│   ├── historical_data.csv
│
├── Visualisations/
│   ├── final_features_data.csv
│   ├── clustered_data.csv
│
├── Notebook/
│   └── Trader_Performance_vs_Market_Sentiment.ipynb
│
├── Report/
│   ├── trader_analysis_Charts_Tables.pdf
│   ├── WriteUp.pdf
│
├── app.py
├── requirements.txt
```

---

## Setup and Installation

### 1. Clone the repository
```
git clone https://github.com/AnonymousPtr/Trader-Performance-vs-Market-Sentiment/
cd Trader-Performance-vs-Market-Sentiment
```

### 2. Install dependencies
```
pip install -r requirements.txt
```

---

## Running the Project

### Notebook (Analysis)
Open:
```
Notebook/Trader_Performance_vs_Market_Sentiment.ipynb
```

Run all cells sequentially. Ensure datasets are available locally or mounted the ones present in the Datasets/Projects (e.g., Google Drive).

---

### Streamlit Dashboard
Run locally:
```
python -m streamlit run app.py
```

---

## Data

- fear_greed_index.csv — Market sentiment classification  
- historical_data.csv — Trader-level transaction data  

---

## Key Components

### Feature Engineering
- Daily PnL  
- Win rate  
- Trade frequency  
- Average trade size  
- Long/Short ratio  
- Risk proxy:  
  risk_score = avg_trade_size × num_trades  

---

### Analysis
- Performance vs sentiment  
- Behavior vs sentiment  
- Trader segmentation  

---

### Bonus Work
- Predictive model (logistic regression + interactive UI)  
- Clustering (KMeans + PCA visualization)  
- Streamlit dashboard  

---

## Assumptions 
- Analysis is cross-sectional due to limited dates  
- Results highlight behavioral patterns, not predictions  
- Risk score is a proxy due to missing leverage data  
