import openpyxl

from project5 import (
    client_car_func,
    dates_func,
    checklist_func,
    todo_func,
    repaired_func,
    repair_fast_func,
    repair_long_func,
    comment_func,
    run,
)


def get_the_column_letter():
    elements = run()
    return elements

def main_excel():
    elements = get_the_column_letter()
    path = elements.get("path")
    letter = elements.get("letter")
    print(path, letter)
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
    old_client = openpyxl.load_workbook(path, read_only=False)
    # Open first sheet
    f_sheet = old_client.active


    """Inserting dates in columns"""
    rows_date_a = ["H4"]
    for row in rows_date_a:
        f_sheet[row] = all_dates[0]
    rows_date_b = [f"{letter}14", "H5"]
    for row in rows_date_b:
        f_sheet[row] = all_dates[1]


    """Inserting client car's parameters as information"""
    f_sheet[f"{letter}15"] = client_car["Przebieg"]

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


    # Save document as update file
    old_file_name = f"{path}"
    old_client.save(filename=f"{old_file_name}")

if __name__ == "__main_excel__":
    main_excel()