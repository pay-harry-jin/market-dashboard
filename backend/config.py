import os
from pathlib import Path
from dotenv import load_dotenv

# .env 파일은 프로젝트 루트에 위치
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

FRED_API_KEY: str = os.getenv("FRED_API_KEY", "")

# ── GitHub raw 데이터 소스 ─────────────────────────────
# GitHub Actions가 data/ 폴더에 JSON을 커밋하면 여기서 읽음
GITHUB_DATA_REPO: str = os.getenv("GITHUB_DATA_REPO", "pay-harry-jin/market-dashboard")
GITHUB_RAW_BASE: str = f"https://raw.githubusercontent.com/{GITHUB_DATA_REPO}/main/data"

# ── 캐시 TTL (초) ──────────────────────────────────────
# 장중(평일 09:30~16:00 ET)에는 짧게, 야간/주말에는 길게
CACHE_TTL_YAHOO_REALTIME: int = 60        # 1분 (장중 KPI)
CACHE_TTL_YAHOO_HISTORY:  int = 3_600     # 1시간 (차트 히스토리)
CACHE_TTL_FRED_KPI:       int = 3_600     # 1시간 (금리, HY스프레드 등 일별)
CACHE_TTL_FRED_MACRO:     int = 86_400    # 24시간 (CPI, PCE, PPI 월별)

# ── Yahoo Finance 심볼 ───────────────────────────────
YAHOO_SYMBOLS: dict = {
    "vix":     "^VIX",
    "nasdaq":  "^IXIC",
    "russell": "^RUT",
    "gold":    "GC=F",
    "dxy":     "DX-Y.NYB",
}

# ── FRED 시리즈 ID ───────────────────────────────────
FRED_KPI_SERIES: dict = {
    "treasury10y": "DGS10",          # 미국 10년물 국채금리 (일별)
    "hy_spread":   "BAMLH0A0HYM2",   # ICE BofA HY OAS (일별)
    "margin_debt": "RIWFRBSL",       # FINRA Margin Debt (월별)
}

FRED_MACRO_SERIES: dict = {
    "cpi": "CPIAUCSL",  # CPI All Urban Consumers (월별)
    "pce": "PCEPI",     # PCE Price Index (월별)
    "ppi": "PPIACO",    # PPI All Commodities (월별)
}
