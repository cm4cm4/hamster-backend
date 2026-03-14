from fastapi import APIRouter, Query

log_router = APIRouter(prefix="/log")

@log_router.post("/environment")
async def environment(humidity: int, temperature: float, hamster_id: int = Query(default= None, alias='hamster-id')):
    pass