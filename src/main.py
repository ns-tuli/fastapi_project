import os
from fastapi import Depends, FastAPI
from pydantic import BaseModel
from .ai.gemini import Gemini

app = FastAPI()

def load_system_prompt():
    try:
        with open("src/prompts/system_prompt.md", "r") as f:
            return f.read()
    except FileNotFoundError:
        return None
    

system_prompt = load_system_prompt()
gemini_api_key = os.getenv("GEMINI_API_KEY")

if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

ai_platform = Gemini(api_key=gemini_api_key, system_prompt=system_prompt)


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str

@app.get("/")
async def root():
    return {"message": "API is running"}