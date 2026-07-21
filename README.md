# 📎 dropbin

Paste text or shorten a URL — one small app, **shipped properly**.

The application is deliberately simple. The point of this project is everything
around it: Postgres in production, real schema migrations, CI running on every
push, and a live deployment you can click.

> 🚧 Work in progress — milestone checklist below.

## Roadmap

- [x] **M1** — App factory, `/healthz`, test suite, CI green on every push
- [ ] **M2** — Data model + create/view drops (links redirect, pastes render); slug generation with collision handling
- [ ] **M3** — Postgres via docker-compose locally; Alembic migrations
- [ ] **M4** — Expiry logic (expired → 410 Gone, missing → 404)
- [ ] **M5** — Deployed live: Render (app) + Neon (Postgres) — URL goes here
- [ ] **M6** — Rate limiting on creation, architecture notes

## Development

```powershell
py -3.12 -m venv .venv
.venv\Scripts\Activate.ps1
pip install -e ".[dev]"

pytest -v          # run the tests
ruff check .       # lint
flask --app dropbin run --debug   # dev server at http://127.0.0.1:5000
```

## Design notes

**Why one table for links and pastes?** A slug like `/abc123` must resolve to
exactly one thing, so links and pastes share a namespace — which means they
share a table (`drops`, with a `kind` column) rather than being two bolted-on
features.

**Why an explicit link/paste toggle instead of auto-detection?** A paste can
legitimately contain nothing but a URL. Guessing the user's intent from content
is ambiguous; a toggle is predictable.