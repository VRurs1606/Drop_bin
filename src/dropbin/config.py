"""Application configuration, sourced from environment variables.

Twelve-factor style: the same code runs everywhere, and only the environment
differs (local dev, CI, Render). Milestone 2 adds DATABASE_URL here; for now
there's just the secret key.
"""

from __future__ import annotations

import os


class Config:
    # Used by Flask for session signing. The default is fine for local dev;
    # production MUST set a real value via the environment (Render dashboard).
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-not-secret")

    # Placeholder for milestone 2/3:
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///dropbin.db")