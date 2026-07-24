from fastapi import FastAPI

from app.config.setting import settings
from app.api.routes.upload import router as upload_router
from app.api.routes.chat import router as chat_router
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes.health import router as health_router
from app.exceptions.handler import global_exception_handler
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from fastapi.responses import HTMLResponse

app = FastAPI(
    title="AI Knowledge Platform",
    description="""
A Retrieval-Augmented Generation (RAG) API built with FastAPI,
ChromaDB, Sentence Transformers, and Google Gemini.

Features:
- Upload PDF documents
- Semantic Search
- AI-powered Question Answering
- Health Monitoring
""",
    version="1.0.0",
    contact={
        "name": "Akhil",
        "email": "your_email@example.com"
    }
)

app.add_exception_handler(
    Exception,
    global_exception_handler
)

app.include_router(upload_router)
app.include_router(chat_router)
app.include_router(health_router)

templates = Jinja2Templates(directory="app/templates")
app.mount("/static", StaticFiles(directory="app/static"), name="static")

'''@app.get("/")
def home():

    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION
    }'''

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"request": request}
    )


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)