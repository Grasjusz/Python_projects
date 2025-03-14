import openpyxl

from project5 import (
    client_name_func,
    client_car_func,
    dates_func,
    checklist_func,
    todo_func,
    repaired_func,
    repair_fast_func,
    repair_long_func,
    comment_func,
)


def main_excel():
    client = client_name_func()
    client_car = client_car_func()
    all_dates = dates_func()
    car_checklist = checklist_func()
    customer_todo = todo_func()
    repaired = repaired_func()
    repair_recommendation = repair_fast_func()
    repair_in_long_time = repair_long_func()
    last_comments = comment_func()

    # Load the report template
    """Insert informations to report"""
    template = openpyxl.load_workbook(filename="template.xlsx", read_only=False)
    # Open first sheet
    f_sheet = template.active
    # Insert data in proper columns/tables
    """Inserting clients name"""
    client = " ".join(client)
    f_sheet["H6"] = client

    """Inserting dates in columns"""
    rows_date_a = ["H4"]
    for row in rows_date_a:
        f_sheet[row] = all_dates[0]
    rows_date_b = ["H5", "C14"]
    for row in rows_date_b:
        f_sheet[row] = all_dates[1]


    """Inserting client car's parameters as information"""
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
    # Things to repair as fast as possible
    f_sheet["C66"] = repair_recommendation
    # Things good to repair before next audit
    f_sheet["C70"] = repair_in_long_time

    """Comments, informations etc. section"""
    f_sheet["C74"] = last_comments


    # Save document as new file with customer name and car model
    file_name = f"{client}-{client_car['Marka']}-{client_car['Model']}"
    template.save(filename=f"{file_name}.xlsx")

if __name__ == "__main_excel__":
    main_excel()