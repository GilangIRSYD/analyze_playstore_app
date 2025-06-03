from fastapi import APIRouter, Query, Body, Header
from google_play_scraper import app as gplay, reviews as gplayReviews
from google_play_scraper.features.reviews import ContinuationToken
from pydantic import BaseModel
from typing import Optional
from app.helper.utils import (
    dict_to_base64,
    base64_to_obj
)
import logging

GPLAY_DETAIL_REVIEW_LINK_TEMPLATE = "https://play.google.com/store/apps/details?id={appId}&reviewId={reviewId}"
router = APIRouter()

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger("GPLAY")

# GET APP DETAIL
@router.get("/app/{app_id}")
def get_list_reviews(
    app_id: str,
    lang = Header("id"),
    country = Header("id")
):
    logger.debug(app_id)
    detail = gplay(app_id, lang, country)

    
    return {
        "id": detail["appId"],
        "title": detail["title"],
        "summary": detail["summary"],
        "score": detail["score"],
        "scrore_text": f"{detail['score']:.1f}",
        "reviews": detail["reviews"],
        "installs": detail["installs"],
        "url": detail["url"],
        "version": detail["version"],
        "icon": detail["icon"],
        "developer": detail["developer"],
        "similar": "TODO: POINTING TO ENDPOINT SIMILAR"
    }
    

class TokenNext(BaseModel):
    token: str
    lang: str
    country: str
    sort: int
    count: int
    filter_score_with: Optional[str] = None
    filter_device_with: Optional[str] = None


# GET LIST REVIEWS
@router.get("/app/{app_id}/reviews")
def get_reviews(
    app_id: str,
    lang = Header("id"),
    country = Header("id"),
    count: int = Query(2),
    token = Query(None)
):
    if token is not None:
        reviews, token_next = gplayReviews(
            app_id = app_id,
            continuation_token=base64_to_obj(token, TokenNext)
        )
    else:
        reviews, token_next = gplayReviews(
            app_id = app_id,
            lang=lang,
            country=country,
            count=count,
        )

    string_token_next = dict_to_base64({
        "token": token_next.token,
        "lang": token_next.lang,
        "country": token_next.country,
        "sort": token_next.sort,
        "count": token_next.count,
        "filter_score_with": token_next.filter_score_with,
        "filter_device_with": token_next.filter_device_with
    })

    return {
        "token_next": string_token_next,
        "reviews": reviews,
        "count_data": len(reviews)
    }