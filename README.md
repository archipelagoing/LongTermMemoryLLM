# 🚀 DialogLace: AI-Powered Long-Term Memory for LLMs

**DialogLace** is a **long-term memory visualization system** designed to enhance AI conversations by providing structured, persistent memory. It integrates **Google Drive API, embeddings, topic modeling, and conversation graph rendering** to store and retrieve past AI conversations efficiently.

---

## 📌 Features
- **Memory Persistence**: Retains past conversations for seamless recall.
- **Semantic Search & Retrieval**: Uses embeddings to retrieve relevant conversations.
- **Graph-Based Visualization**: Displays conversation flow and connections.
- **Google Drive Integration**: Securely stores chat logs.
- **Fuzzy Search & Concept Similarity**: Enhances lookup accuracy using AI-driven embeddings.

---

## 📌 Project Structure
```
LongTermMemoryLLM/
│── backend/
│   ├── main.py              # FastAPI server
│   ├── vectorize_json.py     # Fetches JSONs from Google Drive & stores embeddings
│   ├── check_chroma.py       # Debugging script for embeddings
│   ├── credentials.json      # Google API credentials (ignored in git)
│   ├── chroma_db/            # ChromaDB storage
│   ├── venv/                 # Virtual environment
│   ├── requirements/         # Python dependencies
│       ├── requirements-base.txt
│       ├── requirements-linux.txt
│       ├── requirements-mac.txt
│       ├── requirements-windows.txt
│       ├── requirements-gpu.txt
│── frontend/
│── README.md
│── .gitignore
```

---

# 🔍 How to Test a Search for Embeddings

## 📌 1. Clone the Repository
```bash
git clone <your-repository-url>
cd LongTermMemoryLLM
```

---

## 📌 2. Set Up a Virtual Environment
```bash
# Navigate to the backend directory
cd backend

# Create a virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

---

## 📌 3. Install Dependencies
```bash
# Linux/macOS users:
chmod +x install-requirements.sh
./install-requirements.sh

# Windows users:
install-requirements.bat
```

---

## 📌 4. Set Up Google Drive API Credentials
1. **Download `credentials.json`** from the shared Google Drive folder.
2. **Move `credentials.json`** into the `backend/` directory.
3. **Ensure `credentials.json` is ignored by Git (verify it's in the `backend/` directory).**

---

## 📌 5. Fetch and Store JSON Embeddings
```bash
python backend/vectorize_json.py
```

🚀 **Expected Output:**
```
📂 Fetching JSON files from Google Drive...
🚀 Found 3 JSON files.
🔽 Downloading chat_log_01.json...
🚀 Embedded message: Hello, how are you?...
🚀 All embeddings stored in ChromaDB!
```

---

## 📌 6. Start the FastAPI Server
```bash
python backend/main.py
```

🚀 **Expected Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

---

## 📌 7. Test the Search API

### 🔹 **Option 1: Use FastAPI Swagger Docs (Sen recommends lmao)**
1. Open your browser:
   ```
   http://127.0.0.1:8000/docs
   ```
2. Find the **`/search`** endpoint.
3. Click **"Try it out"**, enter `"Hello"`, and hit **"Execute"**.
4. 🚀 **Expected Response:**
   ```json
   {
     "matches": [
       "Hello, how are you?",
       "I'm good! How can I help you today?"
     ]
   }
   ```

---

### 🔹 **Option 2: Test via `curl`**
```bash
curl -X 'GET' 'http://127.0.0.1:8000/search/?query=Hello' -H 'accept: application/json'
```

🚀 **Expected Response:**
```json
{
  "matches": [
    "Hello, how are you?",
    "I'm good! How can I help you today?",
    "Tell me a joke."
  ]
}
```

---

## 📌 8. Summary
✔ **Clone the repository** → `git clone <repo-url>`  
✔ **Set up a virtual environment** → `python3 -m venv venv && source venv/bin/activate`  
✔ **Install dependencies** → `./install-requirements.sh` or `install-requirements.bat`  
✔ **Set up Google Drive API credentials** → `credentials.json`  
✔ **Fetch & store embeddings** → `python backend/vectorize_json.py`  
✔ **Start FastAPI server** → `python backend/main.py`  
✔ **Query stored embeddings** using Swagger, or `curl`

🚀 **You're all set!**

