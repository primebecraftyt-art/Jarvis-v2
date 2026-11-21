"""Secure per-user API-key storage using the operating-system keyring."""
from __future__ import annotations
import keyring
from jarvis.core.config import KEYRING_SERVICE

ANTHROPIC_USERNAME = "anthropic_api_key"

def save_anthropic_api_key(api_key: str) -> None:
    """Save an API key in the OS credential store, never in source files."""
    cleaned = api_key.strip()
    if not cleaned:
        raise ValueError("API key cannot be empty.")
    keyring.set_password(KEYRING_SERVICE, ANTHROPIC_USERNAME, cleaned)

def get_anthropic_api_key() -> str | None:
    """Return the saved API key, or None when not configured."""
    return keyring.get_password(KEYRING_SERVICE, ANTHROPIC_USERNAME)

def delete_anthropic_api_key() -> None:
    """Remove the saved key from the OS credential store."""
    try:
        keyring.delete_password(KEYRING_SERVICE, ANTHROPIC_USERNAME)
    except keyring.errors.PasswordDeleteError:
        pass
