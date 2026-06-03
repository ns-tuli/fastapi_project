import os
from fastapi import Depends, FastAPI

app = FastAPI()




@app.get("/")
async def root():
    return {"message": "API is running"}