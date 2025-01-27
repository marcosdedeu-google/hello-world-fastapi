from fastapi import FastAPI

app = FastAPI()
# add comment for build trigger w/o SSL


@app.get("/")
async def root():
    return {"message": "Hello World"}
