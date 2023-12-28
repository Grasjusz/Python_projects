
from project2 import check_language

def main():
    test_check_language()


def test_check_language():

    assert check_language("polski") == "Jakiego języka chcesz się uczyć? angielski lub niemiecki?: "