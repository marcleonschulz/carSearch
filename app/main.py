import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import curd
import models
from database import SessionLocal, engine

load_dotenv()

passwd_env = os.getenv("MY_NICE_PASSWORD")

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = ["*", "*:*", "localhost:5000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/test")
def test():
    response = dict()
    response["hsn"] = "test"
    return response


@app.get("/search-{hsn}-{tsn}")
def search(hsn, tsn):
    return curd.search(hsn.upper(), tsn.upper())


@app.post("/create-list")
def create_list(passwd: str):
    if passwd != passwd_env:
        return {"message": "Wrong password"}
    curd.setup_db()