import os
from typing import Optional

try:
    import google.generativeai as genai
except Exception:
    genai = None

from dotenv import load_dotenv

from .base import AIPlatform


load_dotenv()


class Gemini(AIPlatform):
    def __init__(self, api_key: Optional[str] = None, system_prompt: str = None):
        """Initialize Gemini. If `api_key` is not provided, it will be read from env.

        This constructor will not raise if the API key is missing; instead the
        instance will be created without a configured model so callers can
        decide how to handle missing configuration at runtime.
        """
        self.api_key = api_key or os.getenv("GEMINI_API_KEY")
        self.system_prompt = system_prompt

        if not self.api_key:
            self.model = None
            return

        if genai is None:
            raise RuntimeError("google.generativeai package is not installed")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.5-flash-preview-05-20")

    def chat(self, prompt: str) -> str:
        if not getattr(self, "model", None):
            raise RuntimeError("Gemini model not configured. Set GEMINI_API_KEY and install dependencies.")

        if self.system_prompt:
            prompt = f"{self.system_prompt}\n\n{prompt}"

        response = self.model.generate_content(prompt)
        return response.text