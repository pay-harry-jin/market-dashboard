"""
TTL 기반 인메모리 캐시 (thread-safe, asyncio-safe)
- set(key, value, ttl) : ttl 초 후 만료
- get(key)             : 만료 시 None 반환
- invalidate(key)      : 즉시 삭제
- clear()              : 전체 삭제
"""

import time
import threading
from typing import Any, Optional


class TTLCache:
    def __init__(self) -> None:
        self._store: dict[str, tuple[Any, float]] = {}
        self._lock = threading.Lock()

    def set(self, key: str, value: Any, ttl: int) -> None:
        expire_at = time.monotonic() + ttl
        with self._lock:
            self._store[key] = (value, expire_at)

    def get(self, key: str) -> Optional[Any]:
        with self._lock:
            entry = self._store.get(key)
            if entry is None:
                return None
            value, expire_at = entry
            if time.monotonic() > expire_at:
                del self._store[key]
                return None
            return value

    def invalidate(self, key: str) -> None:
        with self._lock:
            self._store.pop(key, None)

    def clear(self) -> None:
        with self._lock:
            self._store.clear()

    def stats(self) -> dict:
        now = time.monotonic()
        with self._lock:
            total = len(self._store)
            alive = sum(1 for _, (_, exp) in self._store.items() if exp > now)
        return {"total_keys": total, "alive_keys": alive, "expired_keys": total - alive}


# 앱 전역 싱글턴
cache = TTLCache()
