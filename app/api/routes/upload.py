from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.document_service import document_service
from app.config.setting import settings

router = APIRouter()


@router.post(
    "/upload",
    summary="Upload PDF",
    description="Uploads a PDF, extracts text, splits it into chunks, generates embeddings, and stores them in ChromaDB.",
    tags=["Upload"]
)
async def upload_pdf(file: UploadFile = File(...)):

    os.makedirs(settings.UPLOAD_DIR, exist_ok=True)

    file_path = os.path.join(
        settings.UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    chunks = document_service.ingest_pdf(file_path)

    return {
        "success": True,
        "message": "PDF uploaded successfully.",
        "data": {
            "chunks": chunks
        }
    }