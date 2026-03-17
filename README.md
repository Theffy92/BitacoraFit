# BitacoraFit

Nutrition and fitness tracking — a production-ready starter scaffold for Django + HTMX + Tailwind + PostgreSQL + DRF + Celery + Redis.

## Planned MVP Features
1. Weight tracking
2. Meal logging
3. Basic dashboard

## Planned MVP architecture (what this project will become)

- Backend: Django (split settings: `settings/base.py`, `settings/dev.py`, `settings/prod.py`)
- Frontend: Django templates + HTMX for progressive enhancement + Tailwind CSS for styling
- API: Django REST Framework (viewsets + routers)
- Database: PostgreSQL (local via Docker Compose; production via RDS)
- Background jobs: Celery with Redis as broker
- AI: LLM-powered nutrition assistant (pluggable adapters, embeddings, simple RAG support)
- Deploy: Docker + AWS (Elastic Beanstalk / ECS, RDS, S3 for static/media, ElastiCache for Redis)

## Repo layout (target)

- `docker-compose.yml` — services: postgres, redis, web, worker (local)
- `Makefile` — developer convenience targets
- `.env.example` — environment variables (DJANGO_SECRET_KEY, DATABASE_URL, REDIS_URL, OPENAI_API_KEY)
- `pyproject.toml` — Python deps and dev tools
- `pre-commit-config.yaml` — hooks for ruff/black/isort
- `bitacorafit/` (Django project)
	- `settings/` (base.py, dev.py, prod.py)
	- `asgi.py`, `wsgi.py`, `urls.py`, `celery.py`
	- `templates/`, `static/`
- `apps/`
	- `accounts/` — auth, email login (optional), templates
	- `logs/` — Meal, FoodItem, FoodLog, WeightLog, Goal + HTMX views and partials
	- `ai/` — `llm.py`, `embeddings.py`, Celery tasks
	- `api/` — DRF serializers & viewsets
- `scripts/` — bootstrap and helper scripts
- `tests/` — pytest fixtures and tests (models, views, APIs, HTMX partials)

## Quickstart (development)


(To-do)

## Planned HTMX pages & API endpoints (MVP)

- Pages (HTMX-first): `/` (landing), `/dashboard/`, `/logs/food/`, `/logs/food/add/` (modal), `/logs/weight/`, `/goals/`, `/health/`
- API (DRF): `/api/food-items/`, `/api/food-logs/`, `/api/weight-logs/`, `/api/goals/` (Token/JWT-ready)

## AI and background tasks (planned)

- `apps/ai/llm.py` — `parse_free_text_meal_to_items(text: str) -> list[ParsedItem]`, `suggest_meal_under_calories(target_kcal: int)` (placeholders)
- `apps/ai/embeddings.py` — embeddings & RAG helpers
- Celery tasks to wrap LLM calls with retry/backoff

## Developer experience

(To-do)

