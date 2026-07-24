from app.services.document_service import document_service

question = "What is FastAPI?"

results = document_service.search(question)

print(results["documents"][0])