import pytest
from project3 import(
    if_slash,
    split,
    if_have_ext,
    if_proper_ext,
    renaming_checking,
)


def main():
    test_if_slash()
    test_split()
    test_if_have_ext()
    test_if_proper_ext()
    test_renaming_checking()

def test_if_slash():
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
