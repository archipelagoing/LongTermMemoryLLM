from fastapi import FastAPI, HTTPException
import chromadb
from sentence_transformers import SentenceTransformer

app = FastAPI()

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="chroma_db")

# Ensure the collection exists
try:
    collection = chroma_client.get_collection(name="chat_embeddings")
except chromadb.errors.InvalidCollectionException:
    collection = chroma_client.create_collection(name="chat_embeddings")

# Load SentenceTransformers model
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    """Generate an embedding using sentence-transformers."""
    return model.encode(text).tolist()

@app.get("/")
def home():
    return {"message": "Welcome to the DialogLace Search API!"}

@app.get("/search/")
def search_similar_messages(query: str):
    try:
        query_embedding = get_embedding(query)
        
        # Query ChromaDB
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=5
        )

        # Extract stored texts from `metadatas` instead of `documents`
        matches = [metadata["text"] for metadata in results["metadatas"][0] if "text" in metadata]

        return {"matches": matches}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
