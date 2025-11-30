## Tiny API Integration

Install deps (Replit Shell):
pip install -r requirements.txt

Run tests:
python -m unittest -v

Run with live HTTP (if `requests` works):
python -m src.app --todo-id 1

Run offline with mock JSON:
python -m src.app --mock samples/todo1.json
