from google.oauth2 import service_account
from googleapiclient.discovery import build
import os
import json
import io

# Path to credentials.json
CREDENTIALS_PATH = "credentials.json"

if not os.path.exists(CREDENTIALS_PATH):
    raise FileNotFoundError("Error: credentials.json not found!")

# Authenticate with Google Drive API
SCOPES = ["https://www.googleapis.com/auth/drive"]
credentials = service_account.Credentials.from_service_account_file(CREDENTIALS_PATH, scopes=SCOPES)
drive_service = build("drive", "v3", credentials=credentials)

FOLDER_ID = "1DOcJvk6hGXMkilt7WAnt-k4iPc8rpRbY"

# Function to list JSON files in a specific folder
def list_json_files():
    print("Fetching JSON files from Google Drive folder...")
    
    # Google Drive API query to search only inside the specific folder
    query = f"'{FOLDER_ID}' in parents and mimeType='application/json'"
    results = drive_service.files().list(q=query, fields="files(id, name)").execute()
    files = results.get("files", [])

    if not files:
        print("No JSON files found in the folder.")
        return None

    print("JSON Files in Drive Folder:")
    for file in files:
        print(f"- {file['name']} (ID: {file['id']})")
    
    return files

# Function to download a specific JSON file
def fetch_json_file(file_id):
    request = drive_service.files().get_media(fileId=file_id)
    file_content = io.BytesIO(request.execute())
    json_data = json.load(file_content)

    print("\n✅ Successfully retrieved JSON file:")
    print(json.dumps(json_data, indent=4))

# Run the test
if __name__ == "__main__":
    files = list_json_files()
    if files:
        first_file_id = files[0]["id"]
        fetch_json_file(first_file_id)  # Fetch the first JSON file found
