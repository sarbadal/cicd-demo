import pandas as pd
from faker import Faker
from faker_airtravel import AirTravelProvider
from random import randint
from typing import Any

from data_models import Airline


fake = Faker(locale = "en_US")
fake.add_provider(AirTravelProvider)


def get_address(number: int) -> list[dict[str, Any]]:
    address_book: list[dict[str, Any]] = []

    for _ in range(0, number):
        address_entry: dict[str, Any] = {
            "name": fake.name(),
            "house_number": randint(a=1, b=250),
            "street_name": fake.street_name(),
            "city": fake.city(),
            "post_code": fake.postcode(),
            "country": fake.country()
        }
        address_book.append(address_entry)
    return address_book


def get_airline_data(num_rows: int) -> list[Airline]:
    airlines: list = []

    for _ in range(0, num_rows):
        flight: dict[str, Any] = {
            "flight": fake.flight()
        }
        airline = flight["flight"]
        airlines.append(airline)
    return airlines


def main() -> None:
    data = get_address(50)
    # data = get_airline_data(5000)
    data = pd.DataFrame(data)
    # data.to_csv("airlines.csv", index=False)
    print(data.head(n=5))
    # print(data)


if __name__ == "__main__":
    main()
