"""Importing"""
import datetime
import openpyxl
import glob
from openpyxl import load_workbook


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
    def combined_dates(self, accept_date, end_date):
        accept_date = accept_date
        end_date = end_date
        return accept_date, end_date

def main():
    """Check if new or old client and handle it."""
    old_or_new = old_or_new_client_func()
    if old_or_new is True:
        new_client_func() #Todo function with generating new file
    elif old_or_new is False:
        old_client_file_path = getting_old_client_file_func()
        old_client_new_repair_func(old_client_file_path)

    client = client_name_func()
    client_car = client_car_func()
    all_dates = dates_func()
    car_checklist = checklist_func()
    customer_todo = todo_func()
    repaired = repaired_func()
    repair_recommendation = repair_fast_func()
    repair_in_long_time = repair_long_func()
    last_comments = comment_func()
    #Load the report template
    template = openpyxl.load_workbook(filename = "template.xlsx", read_only = False)
    #Open first sheet
    f_sheet = template.active
    #Insert data in proper columns/tables
    """Inserting clients name"""
    client = " ".join(client)
    f_sheet["H6"] = client
    """Inserting dates in columns"""
    rows_date_a = ["H4", "C19"]
    for row in rows_date_a:
        f_sheet[row] = all_dates[0]
    rows_date_b = ["H5", "D14", "C14"]
    for row in rows_date_b:
        f_sheet[row] = all_dates[1]
    """Inserting car parameters"""
    f_sheet["H7"] = client_car["Marka"]
    f_sheet["H8"] = client_car["Rok"]
    f_sheet["H9"] = client_car["Model"]
    f_sheet["H10"] = client_car["VIN"]
    f_sheet["H11"] = client_car["Numer rejestracji"]
    f_sheet["C15"] = client_car["Przebieg"]
    """Inserting fulfilling the checklist"""
    f_sheet["C40"] = car_checklist["Zawieszenie"]
    f_sheet["C41"] = car_checklist["Oświetlenie"]
    f_sheet["C42"] = car_checklist["Klimatyzacja"]
    f_sheet["C43"] = car_checklist["Silnik"]
    f_sheet["C44"] = car_checklist["Koła"]
    f_sheet["C45"] = car_checklist["Hamulce"]
    f_sheet["C46"] = car_checklist["Nadwozie"]
    f_sheet["C47"] = car_checklist["Podwozie"]
    f_sheet["C48"] = car_checklist["Korozja"]

    """Inserting customer todo list, depends of list length"""
    row_cs_todo = 19
    customer_todo_count = 0
    while True:
        f_sheet[f"C{row_cs_todo}"] = customer_todo[customer_todo_count]
        row_cs_todo += 1
        customer_todo_count += 1
        if customer_todo_count == len(customer_todo):
            break

    """Inserting repaired service and cost, depends of list length"""
    while True:
        row_repaired = 51
        for key, value in repaired.items():
            f_sheet[f"B{row_repaired}"] = key
            f_sheet[f"C{row_repaired}"] = value
            row_repaired += 1
        break

    """Repair recommendation"""
    #Things to repair as fast as possible
    f_sheet["C66"] = repair_recommendation
    #Things good to repair before next audit
    f_sheet["C70"] = repair_in_long_time

    """Comments, informations etc. section"""
    f_sheet["C74"] = last_comments

    #Save document as new file with customer name and car model
    file_name = f"{client}-{client_car['Marka']}-{client_car['Model']}"
    template.save(filename=f"{file_name}.xlsx")

"""Check if new or old client()"""
def old_or_new_client_func():
    new_column = input("Czy nowy klient? (y/n)").lower()
    if new_column in  ["n", "nie", "not"]:
        return False
    else:
        return True

"""If old client, get old file report and return path to file"""
def getting_old_client_file_func():
    client_path = glob.glob('**/*.xlsx', recursive = True)
    print(f"Wybierz klienta z listy:")
    order = 1
    book = {}
    for file in client_path:
        print(f"{order}.{file}")
        book.update({order: file})
        order += 1
    chosen_client_file = int(input(f"Wpisz numer klienta z listy: "))
    for ordered_numb, client_dir in book.items():
        if ordered_numb == chosen_client_file:
            print(f"client: {client_dir}")
            return client_dir

"""Insert informations to report"""
def old_client_new_repair_func(client_dir):
    old_client = load_workbook(client_dir, read_only=False)
    # Open first sheet
    f_sheet = old_client.active
    # Insert data in proper columns/tables
    f_sheet["H6"] = "Hello test"
    # Save document as update file
    old_file_name = f"{client_dir}"
    old_client.save(filename=f"{old_file_name}")

"""Handle which column is free and fill it up"""
def which_column_func():
    columns = ["c", "d", "e", "f", "g", "h"]
    wb = load_workbook("file.xlsx", data_only=True)
    sh = wb["Sheet_name"]
    print(sh["x10"].value)


        #TODO next things to fullfill next columns, check which column is free and use it.
        #TODO Make new column func and main with openpyxl in another smallers functions/classes - no big code blocks!


def client_name_func():
    """Obtaining client's detail"""
    client_name = input("Imię i nazwisko klienta: ")
    return Client.client_name(client_name)

def client_car_func():
    """Obtaining vehicle's detail"""
    while True:
        car_param = {"Marka":"brak", "Model":"brak", "Rok":"brak", "Silnik":"brak", "Numer rejestracji":"brak", "VIN":"brak", "Przebieg":"brak"}
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
    """Inputing problems with car and asking if there is more"""
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
    repaired_list = {}
    while True:
        repaired_thing = input("Jaka naprawa została wykonana?: ")
        repaired_cost = input("Jaka jest cena naprawy?: ")
        repaired_list.update({repaired_thing:repaired_cost})
        next_repaired = input("Czy chcesz dodać kolejną naprawę?: y/n ").lower()
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
    """Inputing recommendatiob for long term repair"""
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