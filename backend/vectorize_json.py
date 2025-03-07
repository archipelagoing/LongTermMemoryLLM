import os
import json
import io
import chromadb
from google.oauth2 import service_account
from googleapiclient.discovery import build
from sentence_transformers import SentenceTransformer

# Path to Google Drive credentials
CREDENTIALS_PATH = "credentials.json"

if not os.path.exists(CREDENTIALS_PATH):
    raise FileNotFoundError("Error: credentials.json not found!")

# Authenticate with Google Drive API
SCOPES = ["https://www.googleapis.com/auth/drive"]
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
drive_service = build("drive", "v3", credentials=credentials)


FOLDER_ID = "1DOcJvk6hGXMkilt7WAnt-k4iPc8rpRbY"  
# Initialize ChromaDB
chroma_client = chromadb.PersistentClient(path="chroma_db")
collection = chroma_client.get_or_create_collection(name="chat_embeddings")

# Use SentenceTransformers for embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")

def get_embedding(text):
    """Generate embeddings using a local model."""
    return model.encode(text).tolist()

def list_json_files():
    """Fetch the list of JSON files in the Google Drive folder."""
    print("📂 Fetching JSON files from Google Drive folder...")
    
    query = f"'{FOLDER_ID}' in parents and mimeType='application/json'"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])

    if not files:
        print("❌ No JSON files found in the folder.")
        return []

    print(f"✅ Found {len(files)} JSON files in Drive.")
    return files

def fetch_json_file(file_id):
    """Download a JSON file from Google Drive."""
    request = drive_service.files().get_media(fileId=file_id)
    file_content = io.BytesIO(request.execute())
    json_data = json.load(file_content)
    return json_data

def process_json_files():
    """Fetch JSONs from Drive, embed them, and store in ChromaDB."""
    files = list_json_files()
    if not files:
        return

    for file in files:
        file_id, file_name = file["id"], file["name"]
        print(f"⬇️ Downloading {file_name}...")

        json_data = fetch_json_file(file_id)
        if "messages" in json_data:
            for i, message in enumerate(json_data["messages"]):
                text = message["content"]
                embedding = get_embedding(text)

                # Store in ChromaDB
                collection.add(
                    ids=[f"{file_name}-{i}"],
                    embeddings=[embedding],
                    metadatas=[{"text": text}]
                )
                print(f"✅ Embedded message: {text[:50]}...")

    print("✅ All embeddings stored in ChromaDB!")

if __name__ == "__main__":
    process_json_files()
