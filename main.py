from fastapi import FastAPI


app = FastAPI(title="Part Manager")

@app.get("/")
def root():
    return {"message": "Hello World"}