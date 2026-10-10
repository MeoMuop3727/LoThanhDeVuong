import sys
from pathlib import Path

def _base_dir() -> Path:
    # Packaged using PyInstaller
    if getattr(sys, "frozen", False):
        return Path(sys.executable).resolve().parent

    # Running from source
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "assets").is_dir():
            return parent
    return Path.cwd()

BASE_DIR = _base_dir()

def resource_path(relative: str) -> str:
    """ Read-only file included with the game (assets/...) """
    return str(BASE_DIR / relative)

def save_path(relative: str) -> str:
    """ The save file is always located next to the .exe for easy deletion. """
    p = BASE_DIR / relative
    p.parent.mkdir(parents=True, exist_ok=True)
    return str(p)