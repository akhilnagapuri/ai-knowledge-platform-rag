from app.embeddings.embedding_model import embedding_model

text = "FastAPI is a modern Python framework."

embedding = embedding_model.encode(text)

print(type(embedding))
print(len(embedding))
print(embedding[:10])