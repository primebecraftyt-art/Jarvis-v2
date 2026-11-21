"""Central application settings and local data paths."""
from __future__ import annotations
import os
from pathlib import Path

APP_NAME = "Jarvis"
APP_VERSION = "0.1.0"
KEYRING_SERVICE = "JarvisDesktopAssistant"

def get_data_dir() -> Path:
    """Return a per-user application data directory and create it."""
    if os.name == "nt":
        base = Path(os.environ.get("APPDATA", Path.home() / "AppData" / "Roaming"))
    else:
        base = Path(os.environ.get("XDG_CONFIG_HOME", Path.home() / ".config"))
    data_dir = base / APP_NAME
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir

DATA_DIR = get_data_dir()
MEMORY_FILE = DATA_DIR / "memory.json"
LOG_FILE = DATA_DIR / "jarvis.log"
