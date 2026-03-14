from fastapi import FastAPI
from routers import log
app = FastAPI()
app.include_router(log.log_router)
@app.get('/status')
async def root():   
    return {'status':'im alive'}