import os
from pathlib import Path
from fastapi import FastAPI
from pydantic import BaseModel

from dotenv import load_dotenv

load_dotenv()

app = FastAPI()


def load_system_prompt() -> str | None:
    base = Path(__file__).resolve().parent
    prompt_path = base / "prompts" / "system_prompt.md"
    try:
        return prompt_path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return None


def create_ai_platform():
    """Attempt to create a Gemini instance. Returns None on failure.

    This delays importing the optional `google.generativeai` dependency and
    avoids raising at module import time so the app can start even when the
    key or package is missing.
    """
    gemini_api_key = os.getenv("GEMINI_API_KEY")
    system_prompt = load_system_prompt()

    try:
        from .ai.gemini import Gemini

        return Gemini(api_key=gemini_api_key, system_prompt=system_prompt)
    except Exception:
        return None


ai_platform = create_ai_platform()


class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
async def root():
    return {"message": "API is running"}