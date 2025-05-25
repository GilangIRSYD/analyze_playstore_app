from typing import Type, TypeVar
from pydantic import BaseModel
import json
import base64

def dict_to_base64(data: dict) -> str:
    json_str = json.dumps(data)
    base64_str = base64.b64encode(json_str.encode('utf-8')).decode('utf-8')
    return base64_str


T = TypeVar("T", bound=BaseModel)
def base64_to_obj(base64_str: str, model: Type[T]) -> T:
    json_str = base64.b64decode(base64_str).decode('utf-8')
    return model.model_validate_json(json_str)