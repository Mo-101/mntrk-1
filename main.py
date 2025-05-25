import os
import firebase_admin
from firebase_admin import credentials, firestore
from firebase_admin.exceptions import FirebaseError

cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "firebase_key.json")

if not firebase_admin._apps:
    try:
        cred = credentials.Certificate(cred_path)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    except FileNotFoundError:
        raise RuntimeError(f"Firebase key file not found at: {cred_path}")
    except FirebaseError as e:
        raise RuntimeError(f"Failed to initialize Firebase: {e}")
else:
    db = firestore.client()
