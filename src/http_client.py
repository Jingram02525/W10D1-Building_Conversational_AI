import json
from typing import Any, Dict

try:
    import requests
except Exception:
    requests = None

class HttpError(Exception):
    pass

def fetch_todo(todo_id: int, timeout: int = 5) -> Dict[str, Any]:
    """
    Tiny example using a public test API (JSONPlaceholder).
    Returns a dict. Raises HttpError on failure.
    """
    if requests is None:
        raise HttpError("HTTP disabled or requests not installed. Use --mock instead.")

    url = f"https://jsonplaceholder.typicode.com/todos/{todo_id}"
    try:
        resp = requests.get(url, timeout=timeout)
        if resp.status_code != 200:
            raise HttpError(f"HTTP {resp.status_code}: {resp.text[:80]}")
        return resp.json()
    except Exception as e:
        raise HttpError(f"Network error: {e}")

def load_mock(path: str) -> Dict[str, Any]:
    """Local fallback: read a JSON file shipped with your repo."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
