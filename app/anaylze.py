# python lib

# 3rd party lib
from fastapi import APIRouter, Query, Body, Header, Depends
from sqlalchemy.orm import Session

# internal project lib
from app import schemas
from app.gplay import fetch_reviews
from app.models import Application, Review
from app.config.database import get_db
from app.helper.network import success_response, error_response


router = APIRouter()

@router.post("/analyses")
def post_analyses(db: Session = Depends(get_db), payload: schemas.PostAnalyzeRequest = None):
    application = db.query(Application).filter(Application.application_id == payload.application_id).first()
    
    print(application)
    if not application:
        # Do Scraping
        reviews, string_token = fetch_reviews(app_id=payload.application_id, count=2)
        print("Do scrape & analysis")
        response = success_response({
            "reviews": reviews,
            "token": string_token
        })
    else:
        print("select anlysis limit 2000")
        # reviews = db.query(Review).filter(Review.application_id == application.application_id).limit(2000)
        response = success_response("select analusis")
    
        
    return response