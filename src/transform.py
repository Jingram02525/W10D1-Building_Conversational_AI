from typing import Any, Dict


def summarize_todo(todo: Dict[str, Any]) -> str:
    """
    Input: {"id": 1, "title": "...", "completed": true}
    Output: "[DONE] #1: Title"
    Pure: no I/O, no network, no prints.
    """
    tid = todo.get("id", "?")
    title = (todo.get("title") or "").strip() or "Untitled"
    completed = bool(todo.get("completed", False))
    status = "[DONE]" if completed else "[TODO]"
    return f"{status} #{tid}: {title}"
