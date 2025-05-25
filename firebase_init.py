# firebase_init.py
import os, json
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.exceptions import FirebaseError

# Try a JSON blob first (safer in CI/CD), else fall back to a file path
key_json = os.getenv("FIREBASE_KEY_JSON")
key_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if key_json:
    try:
        info = json.loads(key_json)
        cred = credentials.Certificate(info)
    except json.JSONDecodeError as e:
        raise RuntimeError("🔥 FIREBASE_KEY_JSON is not valid JSON") from e

elif key_path:
    if not os.path.exists(key_path):
        raise RuntimeError(f"🔑 Key file not found at {key_path}")
    cred = credentials.Certificate(key_path)

else:
    raise RuntimeError(
        "No Firebase creds found. Set FIREBASE_KEY_JSON or GOOGLE_APPLICATION_CREDENTIALS."
    )

if not firebase_admin._apps:
    try:
        firebase_admin.initialize_app(cred)
    except FirebaseError as e:
        raise RuntimeError(f"Failed to init Firebase: {e}")

# Export the DB client
db = firestore.client()
