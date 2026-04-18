from fastapi import FastAPI
import random

app = FastAPI()

@app.get("/forex_data")
def get_data():
    # Example JSON: Real-time la indha data-va unga AI model/logic tharum
    return {
        "price": 1.0850,
        "candles": [
            {"open": 1.0840, "high": 1.0860, "low": 1.0835, "close": 1.0855},
            # Inga pala candles data varum...
        ],
        "patterns": [
            {"type": "SMC_OB", "top": 1.0865, "bottom": 1.0855, "color": "#FF0000"}, # Order Block
            {"type": "FVG", "top": 1.0845, "bottom": 1.0830, "color": "#00FF00"}     # Fair Value Gap
        ],
        "prediction": "Next Movement: Bullish (90% Confidence)"
    }
