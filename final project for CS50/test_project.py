import pytest
from project import exit_program, check_language, chosen_lang, lang_selection

def test():
    test_exit()
    test_check_language()
    test_check_language_error()
    test_chosen_lang()
    test_lang_selection_different_input()
    
def test_exit():    
    with pytest.raises(SystemExit) as exitprogram:
        exit_program()
    assert exitprogram.type == SystemExit    
    assert exitprogram.value.code == 0

def test_check_language():
    assert check_language("polski") == 'Jakiego języka chcesz się uczyć? angielski lub niemiecki?: '
    assert check_language("english") == 'Which language would you like to learn? polish or german?: '
    assert check_language("deutsch") == 'Welches Sprache möchtest du lernen? polnisch oder englisch?: '

def test_check_language_error():
    assert check_language(" ") == 'Try again, press any key...'
    assert check_language(" 123 ") == 'Try again, press any key...'
    assert check_language("test") == 'Try again, press any key...'
    
def test_chosen_lang():
    file_level = "level1ś.csv"
    assert chosen_lang("angielski")[0] == (file_level)
    
    
def test_lang_selection_different_input():
    assert lang_selection("francais") is None