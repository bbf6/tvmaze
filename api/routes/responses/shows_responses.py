from pydantic import BaseModel
from typing import List, Optional

class Search(BaseModel):
    id: int
    name: str
    channel: str
    summary: Optional[str]
    genres: List[str]

search_response = List[Search]
