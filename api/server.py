from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Pesapal RDBMS API running"}
