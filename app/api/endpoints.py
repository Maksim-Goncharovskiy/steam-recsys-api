from fastapi import APIRouter, HTTPException
from app.models.schemas import RecommendationRequest
from app.services import RecsysService
from steam_content_based_recsys import GameNotFound


router = APIRouter()


@router.post("/recsys/v1/")
async def recsys_v1_handler(request: RecommendationRequest):
    try:
        service = RecsysService()
        return service.recommend(request=request, recsys_version='v1')
    except GameNotFound as err:
        raise HTTPException(status_code=400, detail=str(err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))



@router.post("/recsys/v2/")
async def recsys_v2_handler(request: RecommendationRequest):
    try:
        service = RecsysService()
        return service.recommend(request=request, recsys_version='v2')
    except GameNotFound as err:
        raise HTTPException(status_code=400, detail=str(err))
    except Exception as err:
        raise HTTPException(status_code=500, detail=str(err))
