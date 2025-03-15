from project5 import(
Client,
client_car_func,
dates_func,
checklist_func,
todo_func,
repaired_func,
repair_fast_func,
repair_long_func,
comment_func,
)


def test():
    test_client_name
    test_client_car_func
    test_date
    test_checklist_func
    test_todo_func
    test_repaired_func
    test_repair_fast
    test_repair_long
    test_comment_func
    
    
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
    customer_report = ["brak sprzęgła"]
    assert todo_func() == customer_report
    
def test_repaired_func():
    """running pytest with -s and desired inputs"""
    repaired_list = ["wycieki z silnika", "wymiana filtrów"]
    assert repaired_func() == repaired_list
    
def test_repair_fast():
    """running pytest with -s and desired inputs"""
    to_repair_fast = "hamulce, zawieszenie"
    assert repair_fast_func() == f"Pilne naprawy które należy wykonać jak najszybciej: {to_repair_fast}"

def test_repair_long():
    """running pytest with -s and desired inputs"""
    to_repair_in_time = "wycieki z silnika"
    assert repair_long_func() == f"Przed następnym przeglądem należy naprawić: {to_repair_in_time}"

def test_comment_func():
    """running pytest with -s and desired inputs"""
    comments = "testowy koment"
    assert comment_func() == f"Komentarz, dodatkowe informacje: {comments}"

