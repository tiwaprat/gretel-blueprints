from random import random

import requests
from faker import Faker

faker = Faker()


def get_bike_orders(count=0):
    current = 0
    while count == 0 or current < count:
        gender = 'F' if random() < 0.5 else 'M'
        yield {
            "CustomerID": faker.pyint(10000, 99999),
            "Title": None,
            "FirstName": faker.first_name_female() if gender == 'F' else faker.first_name_male(),
            "MiddleName": (faker.first_name_female() if gender == 'F' else faker.first_name_male())
            if random() < 0.5 else None,
            "LastName": faker.last_name(),
            "Suffix": None,
            "AddressLine1": faker.street_address(),
            "AddressLine2": None,
            "City": faker.city(),
            "StateProvinceName": faker.state(),
            "CountryRegionName": "United States",
            "PostalCode": faker.zipcode(),
            "PhoneNumber": faker.phone_number(),
            # "BirthDate": f"{faker.pyint(1930, 2010)}-{faker.pyint(1, 12):02}-{faker.pyint(1, 28):02}",
            "Education": faker.random.choice(["High School", "College Degree", "Graduate Degree"]),
            "Occupation": faker.random.choice(["Disk Jockey", "Burger Jockey", "Thrill Jockey", "Jockey"]),
            "Gender": gender,
            "MaritalStatus": "S" if random() < 0.5 else "M",
            "HomeOwnerFlag": 0 if random() < 0.5 else 1,
            "NumberCarsOwned": faker.pyint(0, 4),
            "NumberChildrenAtHome": faker.pyint(0, 4),
            "TotalChildren": faker.pyint(0, 4),
            "YearlyIncome": faker.pyint(10000, 999999),
            "ExtraText": f"My other address is {faker.ipv4()}." if random() < 0.025 else "Blah blah blah!"
        }
        if count > 0:
            current += 1


def log_bike_order(order):
    url = 'http://localhost:8080'
    r = requests.post(url, data=order)
    if r.status_code != requests.codes.ok:
        print(f"Response {r.status_code} for order {order}")


if __name__ == "__main__":
    for order in get_bike_orders(count=1000):
        log_bike_order(order)
