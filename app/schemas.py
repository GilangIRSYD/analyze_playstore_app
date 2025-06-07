from pydantic import BaseModel
from typing import Optional

class PostAnalyzeRequest(BaseModel):
    application_id: str