"""Jarvis desktop assistant entry point."""
from __future__ import annotations
import customtkinter as ctk
from jarvis.core.config import APP_NAME, APP_VERSION

def main() -> None:
    """Start the initial Jarvis application shell."""
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")
    app = ctk.CTk()
    app.title(f"{APP_NAME} {APP_VERSION}")
    app.geometry("900x600")
    app.minsize(720, 480)
    ctk.CTkLabel(app, text="JARVIS", font=ctk.CTkFont(size=32, weight="bold")).pack(pady=(48, 12))
    ctk.CTkLabel(app, text="Project setup complete. AI chat arrives in Step 2.").pack(pady=8)
    app.mainloop()

if __name__ == "__main__":
    main()
