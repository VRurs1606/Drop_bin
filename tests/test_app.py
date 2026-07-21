"""Milestone 1 tests: the app starts, routes respond, factory isolates config."""

from __future__ import annotations

from dropbin import create_app


def test_healthz(client):
    r = client.get("/healthz")
    assert r.status_code == 200
    assert r.get_json() == {"ok": True}


def test_index_responds(client):
    r = client.get("/")
    assert r.status_code == 200


def test_factory_applies_overrides():
    app = create_app({"TESTING": True, "CUSTOM_FLAG": 42})
    assert app.config["CUSTOM_FLAG"] == 42


def test_unknown_route_is_404(client):
    assert client.get("/definitely-not-a-thing").status_code == 404