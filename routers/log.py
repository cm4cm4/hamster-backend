from fastapi import APIRouter, Query, Response, status
from .models import log
import sqlite3
from datetime import datetime

db = sqlite3.connect("hamster.db")
cursor = db.cursor()
log_router = APIRouter(prefix="/log")

@log_router.post("/environment")
async def environment(env: log.Environment, r: Response):
    try:
        cursor.execute("INSERT INTO environment (hamster_id, temperature, humidity, time) VALUES (?,?,?,?);",
                        (env.hamster_id, env.temperature, env.humidity, str(datetime.now())))
        db.commit()
        r.status_code = status.HTTP_201_CREATED
        return "Sucessfuly writted log :)"
    except Exception as E:
        r.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        db.rollback()
        cursor.close()
        return "Failed to write to database: " + str(E)
  
         