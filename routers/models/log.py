from pydantic import BaseModel

class Environment(BaseModel):
    temperature: float
    humidity: int
    hamster_id: int