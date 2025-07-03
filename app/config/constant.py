import os

from dotenv import load_dotenv

load_dotenv(override=True)

REDIS_URL=os.getenv("REDIS_URL")

def get_review_detail_url(app_id : str, review_id: str):
    return os.getenv("REVIEW_DETIAL_URL").format(APP_ID=app_id, REVIEW_ID=review_id)

