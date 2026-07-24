from app.services.document_service import document_service
from app.repositories.chroma_repository import chroma_repository

count = document_service.ingest_pdf(
    "uploads/sample.pdf"
)

print(f"Chunks Stored: {count}")

print(f"Database Count: {chroma_repository.count()}")
