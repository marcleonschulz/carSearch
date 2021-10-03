import models, schemas
from sqlalchemy.orm import Session


def search(db: Session, hsn, tsn):
    hersteller_search = db.query(models.Hersteller).filter(models.Hersteller.hsn == hsn).first()
    if hersteller_search is None:
        return {"error": "Der Hersteller wird nicht gefunden"}
    car_search = db.query(models.Car).filter(models.Car.tsn == tsn).filter(
        models.Car.owner_id == hersteller_search.id).first()
    if car_search is None:
        return {"error": "Das Auto wurde nicht gefunden"}
    return {"handel_name": car_search.handelsname, "hersteller_name": hersteller_search.hersteller_name}


def create_car_schema(db: Session, car: schemas.CarCreate, hs_schema: schemas.HerstellerCreate):
    hersteller_search = db.query(models.Hersteller).filter(
        models.Hersteller.hersteller_name == hs_schema.hersteller_name).first()

    if hersteller_search is None:
        db.add(models.Hersteller(
            hersteller_name=hs_schema.hersteller_name,
            hsn=hs_schema.hsn
        ))
        db.commit()

    hersteller_search = db.query(models.Hersteller).filter(
        models.Hersteller.hersteller_name == hs_schema.hersteller_name).first()
    if hersteller_search is None:
        return {"message": "We don't can create the Hersteller"}

    if db.query(models.Car).filter(models.Car.tsn == car.tsn).first() is not None:
        return {"message": "We have this car in the database"}

    db.add(models.Car(
        tsn=car.tsn,
        handelsname=car.handelsname,
        owner_id=hersteller_search.id
    ))
    db.commit()

    if db.query(models.Car).filter(models.Car.tsn == car.tsn).first() is not None:
        return {"message": "car is in"}
    return {"message": "We have a problem"}


def create_car(db: Session, car: models.Car, hs_schema: models.Hersteller, ):
    hersteller_search = db.query(models.Hersteller).filter(
        models.Hersteller.hsn == hs_schema.hsn).first()
    if hersteller_search is None:
        db.add(models.Hersteller(
            hersteller_name=hs_schema.hersteller_name,
            hsn=hs_schema.hsn
        ))
        db.commit()

    hersteller_search = db.query(models.Hersteller).filter(
        models.Hersteller.hersteller_name == hs_schema.hersteller_name).first()
    if hersteller_search is None:
        return {"message": "We don't can create the Hersteller"}
    """
    if db.query(models.Car).filter(models.Car.tsn == car.tsn).first() is not None:
        return {"message": "We have this car in the database"}
    """
    db.add(models.Car(
        tsn=car.tsn,
        handelsname=car.handelsname,
        owner_id=hersteller_search.id
    ))
    db.commit()

    if db.query(models.Car).filter(models.Car.tsn == car.tsn).first() is not None:
        return {"message": "car is in"}
    return {"message": "We have a problem"}
