"""Importing"""
import datetime
import openpyxl


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
    client_car = client_car_func()
    print(client_car, type(client_car))
    #all_dates = dates_func()
    #car_checklist = checklist_func()
    #customer_todo = todo_func()
    #repaired = repaired_func()
    #repair_recommendation = repair_fast_func()
    #repair_in_long_time = repair_long_func()
    #last_comments = comment_func()
    #Load the report template
    template = openpyxl.load_workbook(filename = "template.xlsx")
    #Open first sheet
    f_sheet = template.active
    #Insert data in proper columns/tables
    f_sheet["A1"] = "TEST ! ! !"
    #Save document as new file with customer name and car model
    file_name = f"{''.join(client)}{client_car['Marka']}{client_car['Model']}"
    template.save(filename=f"{file_name}.xlsx")

#to do: rest of editing template





def client_name_func():
    """Obtaining client's detail"""
    client_name = input("Imię i nazwisko klienta: ")
    return Client.client_name(client_name)

def client_car_func():
    """Obtaining vehicle's detail"""
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
    """Obtaining date and checking if proper format"""
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
    """Checklist after car verification"""
    while True:
        car_checklist = {"Zawieszenie":"brak", "Oświetlenie":"brak", "Klimatyzacja":"brak",
                         "Silnik":"brak", "Koła":"brak", "Hamulce":"brak", "Nadwozie":"brak",
                         "Podwozie":"brak", "Korozja":"brak",}
        for key in car_checklist:
            value = input(f"Checklista {key}: ")
            if value:
                car_checklist.update({key: value})
            else:
                print(f"Nie wpisałeś: {key}")
                continue
        break
    return car_checklist

def todo_func():
    """"Inputing problems with car and asking if there is more"""
    todo_list = []
    while True:
        customer_report = input("Awaria, naprawa zgłoszona przez klienta: ")
        todo_list.append(customer_report)
        next_report = input("Chcesz dodać kolejną usterkę? y/n ").lower()
        if next_report == "y":
            continue
        elif next_report != "n":
            continue
        else:
            break
    return todo_list

def repaired_func():
    """Inputing reapired items and asking if more"""
    repaired_list = []
    while True:
        repaired_thing = input("Jakie naprawy zostały wykonane?: ")
        repaired_list.append(repaired_thing)
        next_repaired = input("Czy chcesz dodać kolejną rzecz?: y/n ").lower()
        if next_repaired == "y":
            continue
        elif next_repaired != "n":
            continue
        else:
            break
    return repaired_list

def repair_fast_func():
    """inputing recommendation for short term repair"""
    repair_fast = input("Co należy zrobić jak najszybciej, w pierwszej kolejności?: ")
    recommendation = f"Pilne naprawy które należy wykonać jak najszybciej: {repair_fast}"
    return recommendation

def repair_long_func():
    """"Inputing recommendatiob for long term repair"""
    repair_in_time = input("Co należy naprawić przy następnym przeglądzie?: ")
    recommendation = f"Przed następnym przeglądem należy naprawić: {repair_in_time}"
    return recommendation

def comment_func():
    """Inputing lasts commments"""
    comments = input("Komentarz, dodatkowe informacje: ")
    last_comment = f"Komentarz, dodatkowe informacje: {comments}"
    return last_comment



if __name__ == "__main__":
    main()