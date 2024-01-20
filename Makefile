setup:
	pipenv install

develop:
	pipenv run uvicorn src.app:app --host 0.0.0.0 --port 8000 --reload --reload-dir src --no-access-log

test:
	pipenv run pytest tests