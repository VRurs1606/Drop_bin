"""HTTP routes.

Milestone 1 ships only two endpoints:

* ``/healthz`` — a machine-readable liveness check. CI and Render both use
  this to answer "did the app actually start?", which is why it exists before
  any feature does.
* ``/`` — a placeholder that proves routing + templating are wired up. The
  real form (paste text OR shorten a URL) arrives in milestone 2.
"""

from __future__ import annotations

from flask import Blueprint, jsonify

bp = Blueprint("main", __name__)


@bp.get("/healthz")
def healthz():
    return jsonify(ok=True)


@bp.get("/")
def index():
    # Placeholder until milestone 2 adds the submission form + template.
    return "dropbin — coming soon", 200