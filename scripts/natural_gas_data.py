import requests
import pandas as pd
import yfinance as yf
import time
from dotenv import load_dotenv

# Load environment variables once
load_dotenv('.env')
EIA_API_KEY = os.getenv('EIA_API_KEY')
FRED_API_KEY = os.getenv('FRED_API_KEY')

WORLD_BANK_URL = "http://api.worldbank.org/v2/country/all/indicator/"

# Function to fetch Natural Gas Prices from EIA
def fetch_eia_natural_gas():
    url = f"https://api.eia.gov/v2/seriesid/NG.RNGWHHD.D?api_key={EIA_API_KEY}"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching EIA data:", response.json())
        return pd.DataFrame()
    
    data = response.json()
    
    if "response" not in data or "data" not in data["response"]:
        print("Invalid response format from EIA API")
        return pd.DataFrame()
    
    df = pd.DataFrame(data["response"]["data"])
    df["period"] = pd.to_datetime(df["period"])
    df = df.rename(columns={"period": "Date", "value": "Price"})
    df = df[["Date", "Price"]]
    
    return df.sort_values(by="Date")

# Function to fetch Natural Gas Futures Prices from Yahoo Finance
def fetch_yahoo_natural_gas():
    ng_futures = yf.download("NG=F", start="2000-01-01", end="2025-01-01", interval="1d", auto_adjust=False)
    
    if "Adj Close" in ng_futures.columns:
        ng_futures = ng_futures[["Adj Close"]].reset_index()
    elif "Close" in ng_futures.columns:
        ng_futures = ng_futures[["Close"]].reset_index()
    else:
        print("Error: No valid price column found in Yahoo Finance data.")
        return pd.DataFrame()
    
    ng_futures.columns = ["Date", "Price"]
    return ng_futures

# Function to fetch macroeconomic indicators from FRED
def fetch_fred_data(indicator, name):
    url = f"https://api.stlouisfed.org/fred/series/observations?series_id={indicator}&api_key={FRED_API_KEY}&file_type=json"
    response = requests.get(url)
    data = response.json()
    
    df = pd.DataFrame(data["observations"])
    df["date"] = pd.to_datetime(df["date"])
    df["value"] = pd.to_numeric(df["value"], errors="coerce")
    df = df.rename(columns={"date": "Date", "value": name})
    
    return df

# Function to fetch GDP and Inflation data from World Bank
def fetch_world_bank_data(indicator, name):
    url = f"{WORLD_BANK_URL}{indicator}?format=json&date=2000:2025"
    response = requests.get(url)
    data = response.json()
    
    records = []
    for entry in data[1]:
        if entry["value"]:
            records.append([entry["date"], entry["value"]])
    
    df = pd.DataFrame(records, columns=["Date", name])
    df["Date"] = pd.to_datetime(df["Date"])
    
    return df

# Fetch Data
print("Fetching Natural Gas price data...")
eia_data = fetch_eia_natural_gas()
yahoo_data = fetch_yahoo_natural_gas()

print("Fetching macroeconomic indicators...")
gdp_data = fetch_world_bank_data("NY.GDP.MKTP.CD", "GDP")
inflation_data = fetch_world_bank_data("FP.CPI.TOTL.ZG", "Inflation")
interest_rate_data = fetch_fred_data("FEDFUNDS", "Interest Rate")

# Merge All Data
print("Merging datasets...")
final_df = eia_data.merge(yahoo_data, on="Date", how="outer", suffixes=("_EIA", "_Yahoo"))
final_df = final_df.merge(gdp_data, on="Date", how="left")
final_df = final_df.merge(inflation_data, on="Date", how="left")
final_df = final_df.merge(interest_rate_data, on="Date", how="left")

# Save Data to CSV
final_df.to_csv("data/natural_gas_data.csv", index=False)
print("Data collection complete. File saved as 'natural_gas_data.csv'.")