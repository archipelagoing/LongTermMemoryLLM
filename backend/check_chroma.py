import chromadb

# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_collection(name="chat_embeddings")

# Fetch stored documents
results = collection.get()
print("✅ ChromaDB Stored Data:")
print(results)
