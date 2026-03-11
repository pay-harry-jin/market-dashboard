"""
FRED API 라우터
GET /api/fred/kpi            → 금리, HY스프레드, Margin Debt
GET /api/fred/macro          → CPI / PCE / PPI YoY%
GET /api/fred/history/{id}   → 차트용 히스토리
"""

from fastapi import APIRouter, HTTPException, Query
from backend.services import fred_svc

router = APIRouter(prefix="/api/fred", tags=["FRED"])


@router.get("/kpi")
async def get_fred_kpi():
    """10년물 국채금리, HY Spread OAS, Margin Debt KPI. 캐시 TTL: 1시간"""
    try:
        return await fred_svc.get_kpi_all()
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))


@router.get("/macro")
async def get_fred_macro():
    """CPI / PCE / PPI YoY% 및 MoM%. 캐시 TTL: 24시간"""
    try:
        return await fred_svc.get_macro_all()
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))


@router.get("/history/{series_id}")
async def get_fred_history(
    series_id: str,
    months: int = Query(default=24, ge=3, le=120, description="히스토리 기간(개월)"),
):
    """
    차트용 히스토리 반환.
    series_id: DGS10 | BAMLH0A0HYM2 | RIWFRBSL | CPIAUCSL | PCEPI | PPIACO
    """
    try:
        return await fred_svc.get_history(series_id, months=months)
    except RuntimeError as e:
        raise HTTPException(status_code=503, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
