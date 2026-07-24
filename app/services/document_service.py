import uuid

from app.utils.pdf_reader import pdf_reader
from app.utils.text_chunker import text_chunker
from app.embeddings.embedding_model import embedding_model
from app.repositories.chroma_repository import chroma_repository
from app.prompts.prompt_template import prompt_template
from app.llm.gemini import gemini_client
from app.core.logger import logger


class DocumentService:

    def ingest_pdf(self, file_path: str):

        text = pdf_reader.read(file_path)
        logger.info("PDF text extracted successfully")

        chunks = text_chunker.chunk_text(text)
        logger.info(f"Created {len(chunks)} text chunks")

        # Create one unique ID for each chunk
        ids = [
            str(uuid.uuid4())
            for _ in chunks
        ]

        # Generate embeddings for all chunks in a single call
        embeddings = embedding_model.encode(chunks)
        logger.info("Embeddings generated successfully")

        chroma_repository.add_documents(
            ids=ids,
            documents=chunks,
            embeddings=embeddings
        )
        logger.info("Embeddings stored in ChromaDB")

        return len(chunks)

    def search(self, question: str):

        logger.info(f"Searching for: {question}")

        embedding = embedding_model.encode(question)

        results = chroma_repository.search(embedding)

        logger.info("Relevant documents retrieved")

        return results

    def ask(self, question: str):

        logger.info("Generating AI response")

        results = self.search(question)

        documents = results["documents"][0]

        context = "\n\n".join(documents)

        prompt = prompt_template.build_prompt(
            context=context,
            question=question
        )

        answer = gemini_client.generate(prompt)

        logger.info("Gemini response generated successfully")

        return answer


document_service = DocumentService()