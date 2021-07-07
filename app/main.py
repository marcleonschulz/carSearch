import models, curd, csv
import schemas
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv


load_dotenv()

passwd_env = os.getenv("MY_NICE_PASSWORD")

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/test")
def test():
    return {"hsn": "test"}

@app.get("/search-{hsn}-{tsn}")
def search(hsn, tsn, db: Session = Depends(get_db)):
    return curd.search(db, hsn, tsn)

"""
@app.post("/new-password")
def new_pass(new_pass: str, old_pass: str):
"""


@app.post("/create-list")
def create_list(passwd: str, db: Session = Depends(get_db)):
    if passwd == passwd_env:
        pass
    else:
        return {"message": "Wrong password"}
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        i = 0
        for row in csv_reader:
            i = i + 1
            curd.create_car(db, models.Car(
                tsn=row[2],
                handelsname=row[3]
            ), models.Hersteller(
                hsn=row[0],
                hersteller_name=row[1]
            ))
        return {"message": f"we write {i} cars"}