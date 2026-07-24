from app.services.document_service import document_service

question = "in which years the india won world cups ?"

answer = document_service.ask(question)

print(answer)