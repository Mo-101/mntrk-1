from fastapi import FastAPI
from firebase_init import db

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Mastomy Natalensis DeepSight Awakens!"}

@app.get("/check-firestore")
def check_firestore():
    # Sample Firestore read
    docs = db.collection("test-collection").stream()
    data = [doc.to_dict() for doc in docs]
    return {"documents": data}
