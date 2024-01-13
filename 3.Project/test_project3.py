import pytest
from project3 import(
    if_slash,
    split,
    if_have_ext,
    if_proper_ext,
    renaming_checking,
)


def main():
    test_if_incorrect_slash()
    test_if_slash()
    test_split()
    test_if_have_ext()
    test_if_proper_ext()
    test_renaming_checking()

def test_if_incorrect_slash():
    assert if_slash("test]") == "test/"
    assert if_slash("test:") == "test/"
    assert if_slash("test\\") == "test/"
    assert if_slash("test?") == "test/"
    assert if_slash("test;") == "test/"
    assert if_slash("test#") == "test/"
    assert if_slash("test$") == "test/"
    assert if_slash("test@") == "test/"
    assert if_slash("test%") == "test/"
    assert if_slash("test^") == "test/"
    assert if_slash("test&") == "test/"
    assert if_slash("test'") == "test/"
    
def test_if_slash():
    assert if_slash("test") == "test/"
    assert if_slash("test/") == "test/"
    assert if_slash("test0") == "test0/"
    assert if_slash("test999") == "test999/"
    #↓ ↓ ↓for wrong path like "test " ↓ ↓ ↓
    with pytest.raises(FileNotFoundError, match="Error occured, try again"):
        raise FileNotFoundError("Error occured, try again")
    
def test_split():
    assert split(["test.png", "blank.gif", "hello"]) == [["test", "png"], ["blank", "gif"], ["hello"]]
    
    #do poprawy
def test_if_have_ext():
    assert if_have_ext(["test.png", "blank.gif", "hello"]) == ["test.png", "blank.gif",]