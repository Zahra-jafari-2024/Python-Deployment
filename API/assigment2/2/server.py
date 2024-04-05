from fastapi import FastAPI
app=FastAPI()
@app.get("/maryam")
def read_root():
    return "Hello World"