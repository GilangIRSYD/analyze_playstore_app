from fastapi import APIRouter, Query, Body, Header

router = APIRouter()

@router.post("/analyses")
def post_analyses():
    
    return