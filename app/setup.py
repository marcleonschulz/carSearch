import csv
import models
from database import SessionLocal, engine


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


setup_db()
