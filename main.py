from fastapi import FastAPI

app = FastAPI()
#inserting a comment to trigger the webhook


@app.get("/")
async def root():
    return {"message": "Hello World"}
