from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Photon Backend Running Successfully!"}