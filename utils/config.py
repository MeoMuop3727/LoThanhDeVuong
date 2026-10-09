import json
from pathlib import Path

def load_game(path: str) -> dict:
    try:
        with open(path, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_game(path: str, data: dict) -> bool:
    if not Path(path).exists(): return False

    with open(path, "w") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
