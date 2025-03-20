from typing import List, Optional
from pydantic import BaseModel


class AirportAddress(BaseModel):
    airport: str
    iata: str
    icao: str
    city: str
    state: str
    country: str


class Airline(BaseModel):
    airline: str
    origin: AirportAddress
    destination: AirportAddress
    stops: str | int
    price: float | int


class Address(BaseModel):
    name: str
    house_number: int
    street_name: str
    city: str
    post_code: int
    country: str