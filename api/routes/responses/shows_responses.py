from pydantic import BaseModel
from typing import Any, List, Optional

class SearchComment(BaseModel):
    comment: str
    rating: int

class Search(BaseModel):
    id: int
    name: str
    channel: str
    summary: Optional[str]
    genres: List[str]
    comments: Optional[List[SearchComment]]

search_response = List[Search]

class ShowById(BaseModel):
    id: int
    url: str
    name: str
    type: Optional[str]
    language: Optional[str]
    genres: Optional[List[str]]
    status: Optional[str]
    runtime: Optional[int]
    averageRuntime: Optional[int]
    premiered: Optional[str]
    ended: Optional[str]
    officialSite: Optional[str]
    schedule: Optional[Any]
    rating: Optional[Any]
    weight: Optional[int]
    network: Optional[Any]
    webChannel: Optional[str]
    dvdCountry: Optional[str]
    externals: Optional[Any]
    image: Optional[Any]
    summary: Optional[str]
    updated: Optional[int]
