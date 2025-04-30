install:
	pip install --no-cache-dir -r requirements/dev.txt

start:
	uvicorn main:app --reload