import openpyxl

from project5 import(
    client_name_func,
    client_car_func,
    dates_func,
    checklist_func,
    todo_func,
    repaired_func,
    repair_fast_func,
    repair_long_func,
    comment_func,
    run,
    getting_old_client_file_func,
)

def get_the_column_letter():
    elements = run()
    return elements

def main_excel():
    elements= get_the_column_letter()
    path = elements.get("path")
    letter = elements.get("letter")
    print(path, letter) #todo <<< use letter to change the column, path to access to edit file
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
    template = openpyxl.load_workbook(filename=path, read_only=False)
    # Open first sheet
    f_sheet = template.active
    # Insert data in proper columns/tables
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


    """Inserting client car's parameters as information"""
    f_sheet["h7"] = client_car["Marka"]
    f_sheet["h8"] = client_car["Rok"]
    f_sheet["h9"] = client_car["Model"]
    f_sheet["H10"] = client_car["VIN"]
    f_sheet["H11"] = client_car["Numer rejestracji"]
    f_sheet["C15"] = client_car["Przebieg"]
    """Inserting fulfilling the checklist"""
    f_sheet[f"{letter}40"] = car_checklist["Zawieszenie"]
    f_sheet[f"{letter}41"] = car_checklist["Oświetlenie"]
    f_sheet[f"{letter}42"] = car_checklist["Klimatyzacja"]
    f_sheet[f"{letter}43"] = car_checklist["Silnik"]
    f_sheet[f"{letter}44"] = car_checklist["Koła"]
    f_sheet[f"{letter}45"] = car_checklist["Hamulce"]
    f_sheet[f"{letter}46"] = car_checklist["Nadwozie"]
    f_sheet[f"{letter}47"] = car_checklist["Podwozie"]
    f_sheet[f"{letter}48"] = car_checklist["Korozja"]

    """Inserting customer todo list, depends of list length"""
    row_cs_todo = 19
    customer_todo_count = 0
    while True:
        f_sheet[f"{letter}{row_cs_todo}"] = customer_todo[customer_todo_count]
        row_cs_todo += 1
        customer_todo_count += 1
        if customer_todo_count == len(customer_todo):
            break

    """Inserting repaired service and cost, depends of list length"""
    while True:
        row_repaired = 51
        for key, value in repaired.items():
            f_sheet[f"B{row_repaired}"] = key
            f_sheet[f"{letter}{row_repaired}"] = value
            row_repaired += 1
        break

    """Repair recommendation"""
    # Things to repair as fast as possible
    f_sheet[f"{letter}66"] = repair_recommendation
    # Things good to repair before next audit
    f_sheet[f"{letter}70"] = repair_in_long_time

    """Comments, informations etc. section"""
    f_sheet[f"{letter}74"] = last_comments

    # Save document as new file with customer name and car model
    file_name = f"{client}-{client_car['Marka']}-{client_car['Model']}"
    template.save(filename=f"{file_name}.xlsx")

if __name__ == "__main_excel__":
    main_excel()