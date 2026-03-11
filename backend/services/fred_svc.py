"""
FRED 데이터 서비스 (GitHub raw JSON 읽기 방식)

GitHub Actions의 fetch_fred 작업이 data/ 폴더에 JSON을 커밋하면,
백엔드는 raw.githubusercontent.com 에서 해당 파일을 읽는다.

현재 상태: Yahoo 데이터만 Actions에서 수집 중.
FRED 데이터는 추후 fetch_fred.py + workflow 추가 후 활성화 예정.
"""

import logging
from typing import Any

import httpx

from backend.config import (
    GITHUB_RAW_BASE,
    FRED_KPI_SERIES,
    FRED_MACRO_SERIES,
    CACHE_TTL_FRED_KPI,
    CACHE_TTL_FRED_MACRO,
)
from backend.cache import cache

logger = logging.getLogger(__name__)

_CLIENT = httpx.AsyncClient(
    verify=False,
    timeout=15.0,
    follow_redirects=True,
    headers={"User-Agent": "market-dashboard/2.0"},
)

_NOT_READY_MSG = (
    "FRED 데이터가 아직 준비되지 않았습니다. "
    "GitHub Actions에서 fetch_fred 워크플로우를 실행해 주세요."
)


async def _fetch_json(filename: str) -> dict:
    url = f"{GITHUB_RAW_BASE}/{filename}"
    resp = await _CLIENT.get(url)
    if resp.status_code == 404:
        raise FileNotFoundError(f"데이터 파일 없음: {filename} — {_NOT_READY_MSG}")
    resp.raise_for_status()
    return resp.json()


async def get_kpi_all() -> dict[str, Any]:
    """10년물 금리, HY Spread, Margin Debt KPI (GitHub raw → fred_kpi.json)"""
    cache_key = "fred:kpi:all"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    try:
        data = await _fetch_json("fred_kpi.json")
        cache.set(cache_key, data, ttl=CACHE_TTL_FRED_KPI)
        return data
    except FileNotFoundError as e:
        return {
            name: {"name": name, "series_id": sid, "error": str(e)}
            for name, sid in FRED_KPI_SERIES.items()
        }
    except Exception as e:
        logger.error(f"fred_kpi.json 읽기 실패: {e}")
        return {
            name: {"name": name, "series_id": sid, "error": str(e)}
            for name, sid in FRED_KPI_SERIES.items()
        }


async def get_macro_all() -> dict[str, Any]:
    """CPI / PCE / PPI YoY% (GitHub raw → fred_macro.json)"""
    cache_key = "fred:macro:all"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    try:
        data = await _fetch_json("fred_macro.json")
        cache.set(cache_key, data, ttl=CACHE_TTL_FRED_MACRO)
        return data
    except FileNotFoundError as e:
        return {
            name: {"name": name, "series_id": sid, "error": str(e)}
            for name, sid in FRED_MACRO_SERIES.items()
        }
    except Exception as e:
        logger.error(f"fred_macro.json 읽기 실패: {e}")
        return {
            name: {"name": name, "series_id": sid, "error": str(e)}
            for name, sid in FRED_MACRO_SERIES.items()
        }


async def get_history(series_id: str, months: int = 24) -> dict[str, Any]:
    """차트용 히스토리 (GitHub raw → fred_history_{series_id}_{months}.json)"""
    cache_key = f"fred:history:{series_id}:{months}"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    filename = f"fred_history_{series_id}_{months}.json"
    try:
        data = await _fetch_json(filename)
        cache.set(cache_key, data, ttl=CACHE_TTL_FRED_KPI)
        return data
    except FileNotFoundError as e:
        raise FileNotFoundError(str(e))
    except Exception as e:
        logger.error(f"{filename} 읽기 실패: {e}")
        raise
