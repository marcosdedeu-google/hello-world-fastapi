from fastapi import FastAPI

app = FastAPI()
# add comment for build trigger faster


@app.get("/")
async def root():
    return {"message": "Hello World"}
