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

origins = [
    "https://marc-schulz.tech",
    "http://localhost",
    "http://localhost:5000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["POST","GET"],
    allow_headers=["*"],
)

@app.get("/hsn-search-{hsn}")
def search_hsn(hsn):
    search_tmp = curd.search(hsn.upper(), None)
    return {"hsn": search_tmp.hsn,
            "hersteller_name": search_tmp.hersteller_name}

@app.get("/search-{hsn}-{tsn}")
def search(hsn, tsn):
    return curd.search(hsn.upper(), tsn.upper())


@app.post("/create-list")
def create_list(passwd: str):
    if passwd != passwd_env:
        return {"message": "Wrong password"}
    curd.setup_db()