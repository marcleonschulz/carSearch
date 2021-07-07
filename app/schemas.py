from typing import List, Optional

from pydantic import BaseModel


class CarBase(BaseModel):
    handelsname: str
    tsn: str


class CarCreate(CarBase):
    pass


class Car(CarBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class HerstellerBase(BaseModel):
    hsn: str
    hersteller_name: str


class HerstellerCreate(HerstellerBase):
    pass


class Hersteller(HerstellerBase):
    id: int
    cars: List[Car] = []

    class Config:
        orm_mode = True