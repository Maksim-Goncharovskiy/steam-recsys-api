from fastapi import APIRouter, HTTPException


router = APIRouter()


@router.get("/recsys/v1/")
async def recsys_v1_handler():
    return {"msg": "hello from v1"}



@router.get("/recsys/v2/")
async def recsys_v2_handler():
    return {"msg": "hello from v2"}
