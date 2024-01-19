"""importing modules"""
import pytest
from project3 import(
    if_slash,
    split,
#    if_have_ext,
#    if_proper_ext,
#    renaming_checking,
)

def main():
    """test providen func"""
    test_if_incorrect_slash()
    test_if_slash()
    test_split()


def test_if_incorrect_slash():
    """test for slash correct"""
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
    """test if slask and add slash at the end"""
    assert if_slash("test") == "test/"
    assert if_slash("test/") == "test/"
    assert if_slash("test0") == "test0/"
    assert if_slash("test999") == "test999/"
    #↓ ↓ ↓for wrong path like "test " ↓ ↓ ↓
    with pytest.raises(FileNotFoundError, match="Error occured, try again"):
        raise FileNotFoundError("Error occured, try again")

def test_split():
    """test slicikng the strings"""
    assert split(["first.png", "blank.gif", "notphotofolder"]) == [["first", "png"], ["blank", "gif"], ["notphotofolder"]]
