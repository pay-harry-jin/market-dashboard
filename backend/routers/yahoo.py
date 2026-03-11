"""
Yahoo Finance API 라우터
GET /api/yahoo/kpi                    → 전체 KPI (VIX, Nasdaq, Russell, Gold, DXY)
GET /api/yahoo/history/{symbol_key}   → 차트용 히스토리 (period 파라미터)
"""

from fastapi import APIRouter, HTTPException, Query
from backend.services import yahoo_svc

router = APIRouter(prefix="/api/yahoo", tags=["Yahoo Finance"])


@router.get("/kpi")
async def get_yahoo_kpi():
    """전체 Yahoo Finance KPI를 한 번에 반환. 캐시 TTL: 60초"""
    try:
        return await yahoo_svc.get_kpi_all()
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))


@router.get("/history/{symbol_key}")
async def get_yahoo_history(
    symbol_key: str,
    period: str = Query(default="1y", description="yfinance period: 1mo, 3mo, 6mo, 1y, 2y, 5y"),
):
    """
    차트용 주봉 히스토리 반환.
    symbol_key: vix | nasdaq | russell | gold | dxy
    """
    try:
        return await yahoo_svc.get_history(symbol_key, period=period)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
