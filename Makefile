.PHONY: setup run migrate createsuperuser lint fmt

setup:
	python3 -m venv venv
	./venv/bin/pip install -e ".[dev]"
	cp .env.example .env

run:
	./venv/bin/python src/manage.py runserver

migrate:
	./venv/bin/python src/manage.py migrate

createsuperuser:
	./venv/bin/python src/manage.py createsuperuser

lint:
	./venv/bin/ruff check .

fmt:
	./venv/bin/black .
	./venv/bin/ruff check --fix .
