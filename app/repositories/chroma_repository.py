from app.database.chroma import collection


class ChromaRepository:

    def add_documents(self, ids, documents, embeddings):

        collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings
        )

    def count(self):
        return collection.count()

    # NEW
    def search(self, embedding, n_results=5):

        results = collection.query(
            query_embeddings=[embedding],
            n_results=n_results
        )

        return results


chroma_repository = ChromaRepository()