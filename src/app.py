import argparse

from src.transform import summarize_todo


def main():
    parser = argparse.ArgumentParser(
        prog="app",
        description="Capstone CLI — tiny data integration"
    )
    parser.add_argument("--todo-id", type=int, help="Fetch sample TODO by id (uses HTTP)")
    parser.add_argument("--mock", help="Path to local mock JSON file (offline fallback)")
    args = parser.parse_args()

    data = None

    # Try HTTP if --todo-id given
    if args.todo_id is not None:
        try:
            from src.http_client import fetch_todo
            data = fetch_todo(args.todo_id)
        except Exception as e:
            print(f"HTTP unavailable: {e}")

    # Fallback to mock if no data yet
    if data is None:
        if not args.mock:
            parser.print_help()
            print("\nTip: offline? use:  --mock samples/todo1.json")
            return
        from src.http_client import load_mock
        data = load_mock(args.mock)

    print(summarize_todo(data))

if __name__ == "__main__":
    main()
