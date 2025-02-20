# **📌 Brent Oil Price Analysis**  

## **📖 Project Overview**  
This project analyzes **Brent crude oil prices** to understand their relationship with **economic, technological, and political factors**. Using **time series forecasting, econometric models, and machine learning**, we assess **market trends, volatility, and price drivers**.  

🔍 **Key Objectives:**  
✅ Identify historical events that impacted oil prices.  
✅ Apply **ARIMA, GARCH, and LSTM** models for forecasting.  
✅ Analyze macroeconomic influences (GDP, inflation, exchange rates).  
✅ Explore **OPEC policies, geopolitical risks, and renewable energy impacts**.  
✅ Deploy **interactive dashboards** for real-time analysis.  

---

## **📁 Repository Structure**  
```
/brent-oil-analysis
│── data/                  # Raw & processed datasets
│── notebooks/             # Jupyter Notebooks for EDA & modeling
│── src/                   # Python scripts for data processing & model training
│── models/                # Saved machine learning models
│── reports/               # Insights, visualizations, and findings
│── dashboards/            # Streamlit dashboards for interactive analysis
│── README.md              # Project documentation
│── requirements.txt       # Dependencies for the project
│── .gitignore             # Ignore unnecessary files (e.g., large datasets)
```

## **📊 Data Sources**  
The analysis incorporates:  
📌 **Brent Crude Oil Prices** (1987–2022)
📌 **Macroeconomic Indicators** (GDP, inflation, exchange rates) – [FRED]

## **📈 Methodology**  

### **1️⃣ Data Preprocessing**  
✔ Handle missing values & format time-series data.  
✔ Compute **returns, volatility, and trend indicators**.  

### **2️⃣ Exploratory Data Analysis (EDA)**  
✔ Visualize price trends, volatility, and macroeconomic correlations.  
✔ Use **correlation matrices & heatmaps** to assess dependencies.  

### **3️⃣ Time Series Forecasting & Econometric Models**  
✔ **ARIMA (AutoRegressive Integrated Moving Average)** – Trend-based forecasting.  
✔ **GARCH (Generalized Autoregressive Conditional Heteroskedasticity)** – Volatility modeling.  
✔ **VAR (Vector Autoregression)** – Multivariate analysis with GDP, inflation, and exchange rates.  
✔ **LSTM (Long Short-Term Memory)** – Deep learning-based forecasting.  

### **4️⃣ Event-Driven Analysis**  
✔ **Markov-Switching ARIMA** – Detects regime shifts in price volatility.  
✔ **Geopolitical Impact Study** – Examines how sanctions, wars, and OPEC policies affect oil prices.  

### **5️⃣ Model Evaluation & Validation**  
✔ Use **RMSE, MAE, R²** to compare models.  
✔ Perform **backtesting & cross-validation** for robustness.  


## **📌 Getting Started**  

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/SaraFedlu/Change-point-analysis-and-statistical-modelling-of-time-series-data.git
cd Change-point-analysis-and-statistical-modelling-of-time-series-data
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Run Exploratory Data Analysis**
```bash
jupyter notebook notebooks/eda.ipynb
```


## **📌 Contributors**  
👨‍💻 **Sara Fedlu** - Data Science & Machine Learning  


## **📌 License**  
📜 This project is licensed under **MIT License**.  
