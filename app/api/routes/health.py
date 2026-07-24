from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/health",
    summary="Health Check",
    description="Returns the current status of the AI Knowledge Platform service.",
    tags=["Health"]
)
async def health():

    return {
    "success": True,
    "message": "Service is healthy.",
    "data": {
        "status": "healthy",
        "service": "AI Knowledge Platform"
    }
}