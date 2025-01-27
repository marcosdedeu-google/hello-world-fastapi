from fastapi import FastAPI

app = FastAPI()
# add comment for build trigger


@app.get("/")
async def root():
    return {"message": "Hello World"}
