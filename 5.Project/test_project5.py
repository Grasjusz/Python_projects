import pytest

from project5 import(
Client,
client_car_func,
dates_func,
checklist_func,
todo_func,
repaired_func
)


def test():
    test_client_name
    test_client_car_func
    test_date
    test_checklist_func
    test_todo_func
    test_repaired
    test_repair_fast
    test_repair_in_time
    test_comment
    
    
def test_client_name():
    cn = Client
    name = "Anna Kowalska"
    assert cn.client_name(name) == ["Anna", "Kowalska"]
    
def test_client_car_func():
    """running pytest with -s"""
    car_param = {"Marka": "test", "Model": "brak", "Rok": "brak", "Silnik": "brak", "VIN": "brak"}
    assert client_car_func() == car_param

def test_date():
    """running pytest with -s, and desired date"""
    date1 = "01.01.1990"
    date2 = "01.01.2024"
    assert dates_func() == (('Data przyjęcia pojazdu do naprawy: ', date1),('Data wydania pojazdu z naprawy: ', date2))

    
def test_checklist_func():
    """running pytest with -s and desired keys"""
    car_checklist = {"Zawieszenie": "OK", "Oświetlenie": "prawa zarowka", "Klimatyzacja": "brak",
                     "Silnik": "brak", "Koła": "brak", "Hamulce": "brak", "Nadwozie": "brak",
                     "Podwozie": "brak", "Korozja": "brak", }
    assert checklist_func() == car_checklist

def test_todo_func():
    """running pytest with -s and desired keys"""
    customer_report = "brak sprzęgła"
    assert todo_func() == customer_report
    
def test_repaired_func():
    repaired_list = ["wycieki z silnika", "wymiana filtrów"]
    assert repaired_func() == repaired_list
    
def test_repair_fast():
    to_repair_fast = ["hamulce", "zawieszenie"]
    assert repair_fast(to_repair_fast) == ["Jak najszybciej zaleca się naprawę: ", to_repair_fast]

def test_repair_in_time():
    to_repair_in_time = ["światła przód"]
    assert repair_in_time(to_repair_in_time) == ["Zaleca się w przeciągu roku naprawę: ", to_repair_in_time]

def test_comment():
    assert comment("Wszystko wykonano zgodnie z harmonogramem, duza ilość korozji na prograch") == "Wszystko wykonano zgodnie z harmonogramem, duza ilość korozji na prograch"