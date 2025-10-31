# BitacoraFit

Nutrition and fitness tracking with Django + HTMX + Tailwind + PostgreSQL.

## Quickstart

**Requirements:** Python 3.11+

```bash
# 1. Setup virtual environment and install dependencies
make setup

# 2. Start PostgreSQL
docker compose up -d

# 3. Run bootstrap script to create Django project structure
bash scripts/bootstrap.sh

# 4. Run migrations and create superuser
make migrate
make createsuperuser

# 5. Run development server
make run
```

Visit `http://localhost:8000`

## Development

- `make fmt` - Format code with Black and Ruff
- `make lint` - Check code with Ruff

## TODO

- Add Tailwind via npm later
- Configure Celery for background tasks

## Next steps

1. Run `bash scripts/bootstrap.sh`
2. Create `.env` from `.env.example`
3. Add Django settings in `config/settings.py` (DEBUG, DB)
4. Register `logs` app in settings
5. Create first model `FoodItem` and run migrations
6. Add base template and an index view with HTMX snippet
