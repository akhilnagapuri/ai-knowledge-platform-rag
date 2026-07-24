from fastapi import APIRouter

from app.schema.chat import ChatRequest, ChatResponse
from app.services.document_service import document_service

router = APIRouter()


@router.post(
    "/chat",
    summary="Ask a question",
    description="Searches the uploaded documents using semantic search and generates an answer using Gemini AI.",
    tags=["Chat"]
)
async def chat(request: ChatRequest):

    answer = document_service.ask(request.question)

    return {
    "success": True,
    "message": "Answer generated successfully.",
    "data": {
        "answer": answer
    }
}