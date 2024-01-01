import pytest
from project4 import (
    name_func,
    email_func
    )

def test():
    test_name_func()
    test_second_name_func()
    test_email_func()
    
    
def test_name_func():
    level = 1
    assert name_func("Grayszjan", level) == "Grayszjan"
    assert name_func("Test", level) == "Test"
    assert name_func("AYAHUSAKAKBABAY", level) == "AYAHUSAKAKBABAY"
    assert name_func("ABC", level) == "ABC"
    assert name_func("ALAĄĆęłńóŚŹŻ", level) == "ALAĄĆęłńóŚŹŻ"
    
    
def test_second_name_func():
    level = 2
    assert name_func("Grayszjan", level) == "Grayszjan"
    assert name_func("Test", level) == "Test"
    assert name_func("AYAHUSAKAKBABAY", level) == "AYAHUSAKAKBABAY"
    assert name_func("ABC", level) == "ABC"
    assert name_func("ALAĄĆęłńóŚŹŻ", level) == "ALAĄĆęłńóŚŹŻ"
    
    
def test_email_func():
    level = 3
    assert email_func("grayszjan.lipa@o2.pl", level) == "grayszjan.lipa@o2.pl"
