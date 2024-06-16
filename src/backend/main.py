from fastapi import FastAPI # type: ignore
from db import database, engine, metadata
from controllers import user_controller

metadata.create_all(engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user_controller.router, prefix="/users", tags=["users"])

@app.get("/")
def read_root():
    return { "message": "Hello, codando às traças" }