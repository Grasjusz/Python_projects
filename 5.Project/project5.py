"""Importing"""
from mimetypes import inited


class Client:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def client_name(self):
        name = self.split()
        return name

class Client_Car:
    def __init__(self, brand, model, year, engine, vin):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.vin = vin


def main():
    client = client_name_func()
    print(f"{client}")
    client_car = client_car_func()

def client_name_func():
    client_name = input("Imię i nazwisko klienta: ")
    return Client.client_name(client_name)

def client_car_func():
    brand, model, year, engine, vin = input("Marka, Model, Rok, Silnik, Numer VIN: ").split()
    print(brand)
    print(model)
    print(year)
    print(engine)
    print(vin)

if __name__ == "__main__":
    main()