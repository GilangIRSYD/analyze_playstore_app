from app.config.celery_app import celery_app
from app.config.database import get_db_contex

import time

@celery_app.task
def analyze_reviews(app_id):
    with get_db_contex() as db:
        print(app_id)
        scrape_application_detail.delay(app_id)
        task = scrape_reviews.delay(app_id)
    return task.id

@celery_app.task
def scrape_application_detail(app_id):
    print("🤖 Scrapping application details ", app_id)
    time.sleep(5)
    
    return "Scrapping application Done ✅"

@celery_app.task
def scrape_reviews(app_id):
    print("🤖 Scrapping reviews of ", app_id)
    time.sleep(2)
    
    return ["reviews.....","reviews ..."]
    