install:
	pip install --no-cache-dir -r requirements/dev.txt

local:
	uvicorn main:app --reload

build:
	docker compose build

up:
	docker compose up -d

migrate:
	docker compose exec web alembic upgrade head

start: build up migrate