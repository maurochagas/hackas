from fastapi import FastAPI # type: ignore
from fastapi.middleware.cors import CORSMiddleware # type: ignore
from db import database, engine, metadata
from controllers import user_controller, gemini_controller

metadata.create_all(engine)

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(user_controller.router, prefix="/users", tags=["users"])
app.include_router(gemini_controller.router, prefix="/gemini", tags=["gemini"])

@app.get("/")
def read_root():
    return { "message": "Hello, codando às traças" }