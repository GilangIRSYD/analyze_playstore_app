.PHONY: dev start install freeze clean worker flower

# install dependency dari requirements.txt
install:
	pip install -r requirements.txt

# jalankan server di development mode
dev:
	uvicorn main:app --reload

# run worker
worker:
	celery -A app.config.celery_app worker --loglevel=debug --concurrency=2 

# run worker ui
flower:
	celery -A app.config.celery_app flower --port=5555

# jalankan server production mode
start:
	gunicorn -k uvicorn.workers.UvicornWorker main:app --bind 0.0.0.0:8000 --workers 4

# simpan dependency project ke requirements.txt
freeze:
	pip freeze > requirements.txt

# hapus virtual environment & file __pycache__
clean:
	rm -rf venv __pycache__
