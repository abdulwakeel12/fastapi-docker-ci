from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello from version 2 of my FastAPI app!"}

@app.get("/health")
def health():
    return {"status": "ok"}
