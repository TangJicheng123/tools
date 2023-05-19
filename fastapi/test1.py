from fastapi import FastAPI

app = FastAPI()


@app.get("/item/{id}")
async def get_id(id: int):
    print(type(id))
    return {"message": id}