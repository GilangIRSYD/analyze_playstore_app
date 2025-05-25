from fastapi import APIRouter, Header, Query, Body
from pydantic import BaseModel
from typing import Optional

router = APIRouter()

person = {   
        "name": "Gilang",
        "age": 20,
        "hobby": "ngoding"
    }

@router.get("/person")
def get_person():
    return person

@router.get("/person/{key}")
def get_person_by_key(key: str):
    if key in person:
        return { "value": person[key] }
    else:
        return {"error": "Key not found"}
    

@router.post("/person/{key}")
def post_person_key(key:str, value: str):
    person[key] = value
    return person


class DebugItem(BaseModel):
    message: str
    optional: Optional[str] = None

@router.post("/debug/{id}")
def debug_endpoint(
    id: str,                              # Path param
    token: str = Header(None),            # Header param
    flag: bool = Query(False),            # Query param
    item: DebugItem = Body(None)          # Body param
):
    return {
        "path_param_id": id,
        "header_token": token,
        "query_flag": flag,
        "body_content": item.dict() if item else {}
    }

# curl -X POST "http://127.0.0.1:8000/person/123?show=true" \
#      -H "Content-Type: application/json" \
#      -H "token: 12345abcde" \
#      -d '{"key": "nickname", "value": "Andoy"}'
