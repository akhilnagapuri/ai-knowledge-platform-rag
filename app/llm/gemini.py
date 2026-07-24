import google.generativeai as genai

from app.config.setting import settings


class GeminiClient:

    def __init__(self):

        genai.configure(
            api_key=settings.GEMINI_API_KEY
        )

        self.model = genai.GenerativeModel(
            settings.GEMINI_MODEL
        )

    def generate(self, prompt: str):

        response = self.model.generate_content(prompt)

        return response.text


gemini_client = GeminiClient()