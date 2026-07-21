"""dropbin — paste text or shorten a URL.

A deliberately small app whose point is being *shipped properly*: Postgres in
production, schema migrations, CI on every push, and a live deployment. The
application logic stays simple so the engineering around it stays visible.

This module holds the application factory. Using a factory (instead of a
module-level ``app = Flask(...)`` like a tutorial app) means tests can build a
fresh, isolated app with their own config — no ``importlib.reload`` tricks
needed to re-point paths between tests.
"""

from __future__ import annotations

from flask import Flask

from dropbin.config import Config


def create_app(config_overrides: dict | None = None) -> Flask:
    """Build and configure the Flask application.

    Args:
        config_overrides: Optional settings that take precedence over the
            defaults in :class:`Config`. Tests use this to point the app at
            an in-memory database, enable TESTING mode, etc.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    if config_overrides:
        app.config.update(config_overrides)

    from dropbin.routes import bp

    app.register_blueprint(bp)
    return app