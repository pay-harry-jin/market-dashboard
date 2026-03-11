"""
Yahoo Finance 데이터 서비스 (GitHub raw JSON 읽기 방식)

GitHub Actions가 15분마다 data/ 폴더에 JSON을 커밋하면,
백엔드는 raw.githubusercontent.com 에서 해당 파일을 읽는다.

이 방식은 회사 네트워크 프록시(Menlo/Squid)를 우회한다.
raw.githubusercontent.com 은 프록시에서 허용됨.
"""

import logging
from typing import Any, Optional

import httpx

from backend.config import (
    GITHUB_RAW_BASE,
    YAHOO_SYMBOLS,
    CACHE_TTL_YAHOO_REALTIME,
    CACHE_TTL_YAHOO_HISTORY,
)
from backend.cache import cache

logger = logging.getLogger(__name__)

_CLIENT = httpx.AsyncClient(
    verify=False,
    timeout=15.0,
    follow_redirects=True,
    headers={"User-Agent": "market-dashboard/2.0"},
)


async def _fetch_json(filename: str) -> dict:
    """GitHub raw에서 JSON 파일 하나를 가져온다."""
    url = f"{GITHUB_RAW_BASE}/{filename}"
    resp = await _CLIENT.get(url)
    if resp.status_code == 404:
        raise FileNotFoundError(
            f"데이터 파일이 아직 없습니다: {filename}\n"
            "GitHub Actions 워크플로우가 아직 실행되지 않았을 수 있습니다. "
            "레포 Actions 탭에서 'Fetch Market Data'를 수동 실행해 주세요."
        )
    resp.raise_for_status()
    return resp.json()


async def get_kpi_all() -> dict[str, Any]:
    """VIX, Nasdaq, Russell, Gold, DXY KPI 반환 (GitHub raw → yahoo_kpi.json)"""
    cache_key = "yahoo:kpi:all"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    try:
        data = await _fetch_json("yahoo_kpi.json")
    except Exception as e:
        logger.error(f"yahoo_kpi.json 읽기 실패: {e}")
        # 각 심볼에 에러 반환
        return {
            key: {"name": key, "symbol": sym, "error": str(e)}
            for key, sym in YAHOO_SYMBOLS.items()
        }

    cache.set(cache_key, data, ttl=CACHE_TTL_YAHOO_REALTIME)
    return data


async def get_history(symbol_key: str, period: str = "1y") -> dict[str, Any]:
    """차트용 주봉 히스토리 반환 (GitHub raw → yahoo_history_{key}_{period}.json)"""
    if symbol_key not in YAHOO_SYMBOLS:
        raise ValueError(f"Unknown symbol key: {symbol_key}")

    # 프론트가 요청하는 period 값이 히스토리 파일에 없을 수 있으므로 fallback
    valid_periods = ["6mo", "1y", "2y", "5y"]
    if period not in valid_periods:
        period = "1y"

    cache_key = f"yahoo:history:{symbol_key}:{period}"
    cached = cache.get(cache_key)
    if cached is not None:
        return cached

    filename = f"yahoo_history_{symbol_key}_{period}.json"
    try:
        data = await _fetch_json(filename)
    except FileNotFoundError as e:
        raise FileNotFoundError(str(e))
    except Exception as e:
        logger.error(f"{filename} 읽기 실패: {e}")
        raise

    cache.set(cache_key, data, ttl=CACHE_TTL_YAHOO_HISTORY)
    return data
