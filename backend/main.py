"""
글로벌 시장 리스크 대시보드 - FastAPI 앱 진입점

실행:
    uvicorn backend.main:app --reload --port 8000

접속:
    http://localhost:8000          → 대시보드 UI
    http://localhost:8000/docs     → Swagger API 문서
    http://localhost:8000/api/...  → REST API
"""

import logging
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from backend.routers import yahoo, fred
from backend.cache import cache

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)

# ── FastAPI 앱 생성 ──────────────────────────────────────
app = FastAPI(
    title="글로벌 시장 리스크 대시보드 API",
    description="VIX, HY Spread, 국채금리, 달러인덱스, Margin Debt, Russell 2000, 금값, Nasdaq, CPI, PCE, PPI",
    version="2.0.0",
)

# ── CORS (개발 편의용, 프로덕션 시 origins 제한 권장) ───
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

# ── API 라우터 등록 ──────────────────────────────────────
app.include_router(yahoo.router)
app.include_router(fred.router)

# ── 정적 파일 서빙 (frontend/) ───────────────────────────
FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


@app.get("/", include_in_schema=False)
async def serve_index():
    return FileResponse(FRONTEND_DIR / "index.html")


# ── 유틸리티 엔드포인트 ──────────────────────────────────
@app.get("/api/health", tags=["System"])
async def health():
    return {"status": "ok", "cache": cache.stats()}


@app.get("/api/cache/clear", tags=["System"])
async def clear_cache():
    cache.clear()
    logger.info("Cache cleared via API")
    return {"status": "cleared"}


@app.exception_handler(404)
async def not_found_handler(request, exc):
    # SPA fallback: 정적 파일 요청이 아닌 경우 index.html 반환
    if not str(request.url.path).startswith("/api"):
        index = FRONTEND_DIR / "index.html"
        if index.exists():
            return FileResponse(index)
    return JSONResponse(status_code=404, content={"detail": "Not Found"})
