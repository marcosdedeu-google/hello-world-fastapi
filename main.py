from fastapi import FastAPI

app = FastAPI()

# testing
@app.get("/")
async def root():
    return {"message": "Hello World"}
