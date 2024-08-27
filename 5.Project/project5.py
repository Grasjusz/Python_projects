"""Importing"""
import datetime


class Client:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def client_name(self):
        name = self.split()
        return name

class ClientCar:
    def __init__(self, brand, model, year, engine, vin):
        self.brand = brand
        self.model = model
        self.year = year
        self.engine = engine
        self.vin = vin

class Dates:
    def __init__(self, accept_date, end_date):
        self.accept_date = accept_date
        self.end_date = end_date
    def combined_dates(accept_date, end_date):
        accept_date = "Data przyjęcia pojazdu do naprawy: ", accept_date
        end_date = "Data wydania pojazdu z naprawy: ", end_date
        return accept_date, end_date

def main():
    client = client_name_func()
    print(f"{client}")
    client_car = client_car_func()
    print(client_car)
    all_dates = dates_func()
    print(all_dates)
    car_checklist = checklist_func()


def client_name_func():
    client_name = input("Imię i nazwisko klienta: ")
    return Client.client_name(client_name)

def client_car_func():
    while True:
        car_param = {"Marka":"brak", "Model":"brak", "Rok":"brak", "Silnik":"brak", "VIN":"brak"}
        for key in car_param:
            value = input(f"Podaj {key}: ")
            if value:
                car_param.update({key: value})
            else:
                print(f"Nie wpisałeś: {key}")
                continue
        break
    return car_param

def dates_func():
    while True:
        try:
            date_format = "%d.%m.%Y"
            accept_date = input("Data przyjęcia pojazdu DD.MM.RRRR: ")
            accept_date = datetime.datetime.strptime(accept_date, date_format)
            accept_date_new = datetime.datetime.strftime(accept_date, date_format)
            end_date = input("Data wydania pojazdu DD.MM.RRRR: ")
            end_date = datetime.datetime.strptime(end_date, date_format)
            end_date_new = datetime.datetime.strftime(end_date, date_format)
        except ValueError:
            print("Niepoprawny format daty, prawidłowy format: DD.MM.RRRR")
            continue
        break
    return Dates.combined_dates(accept_date_new, end_date_new)

def checklist_func():
    while True:
        car_checklist = {"Zawieszenie":"brak", "Oświetlenie":"brak", "Klimatyzacja":"brak",
                         "Silnik":"brak", "Koła":"brak", "Hamulce":"brak", "Nadwozie":"brak",
                         "Podwozie":"brak", "Korozja":"brak",}
        for key in car_checklist:
            value = input(f"Podaj {key}: ")
            if value:
                car_checklist.update({key: value})
            else:
                print(f"Nie wpisałeś {key}")
                continue
        break
    return car_checklist

if __name__ == "__main__":
    main()