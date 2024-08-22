import pytest

from project5 import(
Client,
client_car_func
)


def test():
    test_client_name
    test_client_car_func
    test_client_car_vin
    test_date
    test_checklist
    test_todo
    test_repaired
    test_repair_fast
    test_repair_in_time
    test_comment
    
    
def test_client_name():
    cn = Client
    name = "Anna Kowalska"
    assert cn.client_name(name) == ["Anna", "Kowalska"]
    
def test_client_car_func():
    car_param = {"Marka": "test", "Model": "brak", "Rok": "brak", "Silnik": "brak", "VIN": "brak"}
    assert client_car_func() == car_param
def test_date():
    assert date("01.02.2024") == ["01", "02", "2024"]
    
def test_checklist():
    check_list = {
        "światła":"ok", 
        "zawieszenie":"ok", 
        "opony":"nie ok"
    }
    assert checklist(check_list) == ["Oświetlenie OK", "Zawieszenie OK", "Opony do wymiany"]

def test_todo():
    fault = "brak sprzęgła"
    assert todo(fault) == ["Usterka zgłoszona przez klienta: ", fault]
    
def test_repaired():
    repaired_parts = ["wycieki z silnika", "wymiana filtrów", "komplet sprzęgło"]
    assert repaired(repaired_parts) == ["Wykonano naprawy: ", repaired_parts]
    
def test_repair_fast():
    to_repair_fast = ["hamulce", "zawieszenie"]
    assert repair_fast(to_repair_fast) == ["Jak najszybciej zaleca się naprawę: ", to_repair_fast]

def test_repair_in_time():
    to_repair_in_time = ["światła przód"]
    assert repair_in_time(to_repair_in_time) == ["Zaleca się w przeciągu roku naprawę: ", to_repair_in_time]

def test_comment():
    assert comment("Wszystko wykonano zgodnie z harmonogramem, duza ilość korozji na prograch") == "Wszystko wykonano zgodnie z harmonogramem, duza ilość korozji na prograch"