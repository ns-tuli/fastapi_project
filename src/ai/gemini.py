import os

import google.generativeai as genai
from dotenv import load_dotenv

from .base import AIPlatform


load_dotenv()

class Gemini(AIPlatform):
    def __init__(self, system_prompt: str = None):
        self.api_key = os.getenv("GEMINI_API_KEY")

        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in .env")

        self.system_prompt = system_prompt

        genai.configure(api_key=self.api_key)

        self.model = genai.GenerativeModel(
            "gemini-2.5-flash-preview-05-20"
        )

    def chat(self, prompt: str) -> str:
        if self.system_prompt:
            prompt = f"{self.system_prompt}\n\n{prompt}"

        response = self.model.generate_content(prompt)
        return response.text