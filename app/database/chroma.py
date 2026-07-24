import chromadb

from app.config.setting import settings

client = chromadb.PersistentClient(
    path=settings.CHROMA_DB_PATH
)

collection = client.get_or_create_collection(
    name="knowledge_base"
)