"""
GitHub Actions에서 실행: Yahoo Finance 데이터 수집 → data/ 폴더에 JSON 저장

수집 항목:
  KPI  : VIX, Nasdaq, Russell 2000, Gold, DXY (최근 5거래일 → 당일 종가 + 변화율)
  히스토리: 위 5개 × 4개 기간(6mo, 1y, 2y, 5y) → 주봉 종가

출력 파일:
  data/yahoo_kpi.json
  data/yahoo_history_{key}_{period}.json  (20개)
"""

import json
import datetime
import sys
import os

import yfinance as yf
import warnings
warnings.filterwarnings("ignore")

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
os.makedirs(DATA_DIR, exist_ok=True)

SYMBOLS = {
    "vix":     "^VIX",
    "nasdaq":  "^IXIC",
    "russell": "^RUT",
    "gold":    "GC=F",
    "dxy":     "DX-Y.NYB",
}

HISTORY_PERIODS = ["6mo", "1y", "2y", "5y"]


def _save(filename: str, data: dict) -> None:
    path = os.path.join(DATA_DIR, filename)
    with open(path, "w") as f:
        json.dump(data, f)
    print(f"  saved {filename} ({len(json.dumps(data))} bytes)")


def _pct_change(curr: float, prev: float):
    if prev is None or prev == 0:
        return None
    return round((curr - prev) / abs(prev) * 100, 4)


def fetch_kpi() -> dict:
    results = {}
    for key, symbol in SYMBOLS.items():
        try:
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="5d", interval="1d", auto_adjust=True)
            hist = hist.dropna(subset=["Close"])
            if hist.empty:
                results[key] = {"name": key, "symbol": symbol, "error": "no data"}
                continue
            curr = round(float(hist["Close"].iloc[-1]), 4)
            prev = round(float(hist["Close"].iloc[-2]), 4) if len(hist) >= 2 else None
            last_date = str(hist.index[-1].date())
            results[key] = {
                "name":       key,
                "symbol":     symbol,
                "current":    curr,
                "prev_close": prev,
                "change_pct": _pct_change(curr, prev),
                "change_abs": round(curr - prev, 4) if prev is not None else None,
                "last_date":  last_date,
            }
            print(f"  KPI {key}: {curr} ({last_date})")
        except Exception as e:
            print(f"  KPI {key} ERROR: {e}", file=sys.stderr)
            results[key] = {"name": key, "symbol": symbol, "error": str(e)}
    return results


def fetch_history(key: str, symbol: str, period: str) -> dict:
    try:
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period=period, interval="1wk", auto_adjust=True)
        hist = hist.dropna(subset=["Close"])
        history = [
            {"date": str(ts.date()), "value": round(float(row["Close"]), 4)}
            for ts, row in hist.iterrows()
        ]
        print(f"  history {key}/{period}: {len(history)} points")
        return {"symbol_key": key, "symbol": symbol, "period": period, "history": history}
    except Exception as e:
        print(f"  history {key}/{period} ERROR: {e}", file=sys.stderr)
        return {"symbol_key": key, "symbol": symbol, "period": period, "history": [], "error": str(e)}


def main():
    print(f"[fetch_yahoo] started at {datetime.datetime.utcnow().isoformat()}Z")

    print("-- KPI --")
    kpi = fetch_kpi()
    kpi["_updated_at"] = datetime.datetime.utcnow().isoformat() + "Z"
    _save("yahoo_kpi.json", kpi)

    print("-- History --")
    for key, symbol in SYMBOLS.items():
        for period in HISTORY_PERIODS:
            data = fetch_history(key, symbol, period)
            _save(f"yahoo_history_{key}_{period}.json", data)

    print(f"[fetch_yahoo] done at {datetime.datetime.utcnow().isoformat()}Z")


if __name__ == "__main__":
    main()
