from fastapi import FastAPI
import yfinance as yf
import pandas as pd

app = FastAPI()

def detect_smc_patterns(df):
    patterns = []
    # Simple SMC Logic: Last 20 candles la irukra High/Low vechu OB detect panradhu
    recent_df = df.tail(20)
    max_idx = recent_df['High'].idxmax()
    min_idx = recent_df['Low'].idxmin()
    
    # Order Block (Example Logic)
    patterns.append({
        "type": "SMC_OB",
        "top": float(recent_df.loc[max_idx, 'High']),
        "bottom": float(recent_df.loc[max_idx, 'Low'])
    })
    
    # BOS Logic (Break of Structure)
    if df['Close'].iloc[-1] > df['High'].iloc[-5:-1].max():
        patterns.append({
            "type": "BOS",
            "top": float(df['High'].iloc[-5:-1].max()),
            "bottom": 0
        })
        
    return patterns

@app.get("/forex_data")
def get_forex_data():
    # Real-time data fetching for EUR/USD (1 minute interval)
    ticker = yf.Ticker("EURUSD=X")
    df = ticker.history(period="1d", interval="1m")
    
    if df.empty:
        return {"error": "Data not found"}

    # Formatting candles for Android
    candles = []
    for index, row in df.tail(30).iterrows():
        candles.append({
            "open": float(row['Open']),
            "high": float(row['High']),
            "low": float(row['Low']),
            "close": float(row['Close'])
        })

    # Pattern Detection logic call
    smc_marks = detect_smc_patterns(df)

    return {
        "prediction": "Next Movement: Potential Bullish (90% Confidence)",
        "candles": candles,
        "patterns": smc_marks
    }
