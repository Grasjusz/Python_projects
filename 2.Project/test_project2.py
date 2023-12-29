import pytest
from project2 import check_language
from project2 import lang_selection

def main():
    test_check_language()
    test_lang_selection()


def test_check_language():

    assert check_language("polski") == "Jakiego języka chcesz się uczyć? angielski lub niemiecki?: "
    assert check_language("english") == "Which language would you like to learn? polish or german?: "
    assert check_language("deutsch") == "Welches Sprache möchtest du lernen? polnisch oder englisch?: "
    with pytest.raises(SystemExit) as ext:
        check_language("exit program")
    assert ext.type == SystemExit
    assert ext.value.code == 0
    
    
def test_lang_selection():
    with pytest.raises(SystemExit) as ext:
        check_language("exit program")
    assert ext.type == SystemExit
    assert ext.value.code == 0