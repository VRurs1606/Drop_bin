"""Shared pytest fixtures.

Each test gets a fresh app built by the factory with test config. This is the
payoff of the factory pattern: isolation comes for free, with no environment
variables or module reloading involved.
"""

from __future__ import annotations

import pytest

from dropbin import create_app


@pytest.fixture
def app():
    return create_app({"TESTING": True})


@pytest.fixture
def client(app):
    return app.test_client()