import csv
import models
from database import SessionLocal, engine


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


def create_error_dict(message):
    response = dict()
    response["error"] = message
    return response


def search(hsn, tsn):
    db = SessionLocal()
    hersteller_search = db.query(models.Hersteller).filter(models.Hersteller.hsn == hsn).first()

    if hersteller_search is None:
        return create_error_dict("Der Hersteller wird nicht gefunden")

    if tsn is None:
        return hersteller_search

    car_search = db.query(models.Car).filter(models.Car.tsn == tsn).filter(
        models.Car.owner_id == hersteller_search.id).first()

    if car_search is None:
        return create_error_dict("Das Auto wurde nicht gefunden")

    response = dict()
    response["handel_name"] = car_search.handelsname
    response["hersteller_name"] = hersteller_search.hersteller_name

    return response


def setup_db():
    db = SessionLocal()
    models.Base.metadata.create_all(bind=engine)
    with open("data.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            tsn = row[2]
            handelsname = row[3]
            hsn = row[0]
            hersteller_name = row[1]
            hersteller: models.Hersteller = db.query(models.Hersteller).filter(models.Hersteller.hsn == hsn).first()
            if hersteller is None:
                db.add(models.Hersteller(hersteller_name=hersteller_name, hsn=hsn))
                db.commit()
                hersteller = db.query(models.Hersteller).filter(models.Hersteller.hsn == hsn).first()
            db.add(models.Car(tsn=tsn, handelsname=handelsname, owner_id=hersteller.id))
    db.commit()
    db.close()
