from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


from database import Base


class Hersteller(Base):

    __tablename__ = "hersteller"


    id = Column(Integer, primary_key=True, index=True)
    hersteller_name = Column(String, unique=True, index=True)
    hsn = Column(String, unique=True, index=True)
    cars = relationship("Car", back_populates="owner")



class Car(Base):

    __tablename__ = "cars"


    id = Column(Integer, primary_key=True, index=True)
    tsn = Column(String, index=True)
    handelsname = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("hersteller.id"))

    owner = relationship("Hersteller", back_populates="cars")
