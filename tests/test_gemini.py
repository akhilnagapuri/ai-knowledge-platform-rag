from app.llm.gemini import gemini_client

response = gemini_client.generate(
    "Explain rag in two sentences."
)

print(response)