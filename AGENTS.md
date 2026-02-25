# AGENTS.md

## Cursor Cloud specific instructions

### Project Overview
Yu Blog (22too.com) — a personal blog platform built with Flask + PostgreSQL + SQLAlchemy + Jinja2. Single monolithic app, no microservices.

### Prerequisites (system-level, already installed in snapshot)
- PostgreSQL 16 (with database `22too` and user `postgres` password `2015`)
- `libpq-dev`, `python3-dev` for building psycopg2 from source
- Python 3.12 virtualenv at `/workspace/venv`

### Key Gotchas
- **Python 2→3 fixes applied**: The original code had Python 2 patterns (implicit relative imports, `urlparse`, `raw_input`, `print` statements). These have been fixed in the codebase.
- **requirements.txt has outdated pinned versions**: Do NOT install `requirements.txt` directly. Use `psycopg2-binary` instead of `psycopg2==2.6`, and updated versions of `MarkupSafe` and `itsdangerous`. See the venv setup in the update script.
- **`werkzeug.contrib.atom`** was removed in Werkzeug 2.0+. The `recent_feed()` endpoint in `view/toole.py` has a fallback that returns 501 when AtomFeed is unavailable.
- **`config.py`** must exist (copied from `config.py.sample`). It is gitignored. DB connection string: `postgresql://postgres:2015@localhost:5432/22too?`
- **PostgreSQL must be running** before starting the app: `sudo pg_ctlcluster 16 main start`

### Running the Dev Server
```bash
source /workspace/venv/bin/activate
python 22.py
```
Runs Flask dev server on `0.0.0.0:2001` with debug mode.

### Database Setup (one-time)
```bash
sudo -u postgres psql -c "ALTER USER postgres PASSWORD '2015';"
sudo -u postgres psql -c "CREATE DATABASE \"22too\";"
source /workspace/venv/bin/activate
python create_table.py
```

### Admin User
Create via script: `python create_root.py` (interactive) or programmatically:
```python
from model.user import User
from app import app
user = User(username='admin')
user.set_password('admin123')
app.DBSession.add(user)
app.DBSession.commit()
```

### No Automated Tests
This codebase does not have a test suite. Manual testing is required via the browser.

### No Linter Configuration
No linter (flake8, pylint, etc.) is configured in this project.
