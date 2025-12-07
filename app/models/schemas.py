from typing import List
from pydantic import BaseModel 


class RecommendationRequest(BaseModel):
    liked_games_ids: List[int]
    m: int = 15


class RecommendationItem(BaseModel):
    rec: int
    src: int