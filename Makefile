install:
	pip install --no-cache-dir -r requirements/dev.txt

build:
	docker compose build

up:
	docker compose up -d

start: build up migrate

migrate:
	docker compose exec web alembic upgrade head

run-test:
	pytest -v