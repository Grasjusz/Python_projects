"""Importing"""
import random
import sys


language_list = ["angielski", "niemiecki", "polish", "german", "polnisch", "englisch"]
word_list: list = []
typed_lang_study: list = []
def main():
    """Main program"""
    while True:
        language = input("Choose your language: polski, english or deutsch: ").lower()
        learn_lang = input(check_language(language)).lower()
        try:
            with open(chosen_lang(learn_lang)[0], "r", encoding="utf-8") as file_level:
                for line in file_level:
                    line = line.lower()
                    pl, eng, de = line.strip().split(",")
                    word_list.append({"pl":pl, "eng":eng, "de":de})
        except (NameError, TypeError):
            print("You need to select the program language: polski, english or deutsch\n"
                  "Musisz wybrać język programu: polski, english lub deutsch\n"
                  "Sie müssen die Programmsprache auswählen: polski, english oder deutsch")
            continue
        else:
            break
    lang_selection(language)

def check_language(language):
    """check chosen language and run proper"""
    translate = {
                 "pl":"Jakiego języka chcesz się uczyć? angielski lub niemiecki?: ",
                 "eng":"Which language would you like to learn? polish or german?: ",
                 "de":"Welches Sprache möchtest du lernen? polnisch oder englisch?: "
                 }
    if language == "polski":
        return translate["pl"]
    if language == "english":
        return translate["eng"]
    if language == "deutsch":
        return translate["de"]
    if language == "exit program":
        exit_program()
    return None

def chosen_lang(learn_lang):
    """Checking and choosing proper file with words and translations"""
    if learn_lang in language_list:
        typed_lang_study.append(learn_lang)
        file_level = "level1.csv"
        return file_level, typed_lang_study
    if learn_lang == "exit program":
        exit_program()
    return None

def lang_selection(language):
    """Chosing proper program function depends of chosen program language and runs the target program(function)"""
    if language == "polski":
        return pol_lang()
    if language == "english":
        return eng_lang()
    if language == "deutsch":
        return de_lang()
    return None

def exit_program():
    """Exit program function"""
    print("Exiting the program...")
    sys.exit(0)

def pol_lang():
    """Shuffling and printing pair of words to print, scoring - ONLY LANGUAGE POLISH"""
    score = 0
    total_points = len(word_list)
    if "angielski" in typed_lang_study:
        while word_list:
            for pair_word in word_list.copy():
                random.shuffle(word_list)
                pl_word = pair_word["pl"]
                eng_word = pair_word["eng"]
                answer = input(f"Tłumaczenie słowa '{eng_word}' brzmi: ").lower()
                if answer == pl_word:
                    word_list.remove(pair_word)
                    score += 1
                    print(f"Twój aktualny wynik {score} z {total_points} punktów")
                elif answer == "exit program":
                    exit_program()
                else:
                    print(f"Poprawne słowo '{pl_word}'")
        return print("Wszystkie słowa poprawnie przetłumaczone, gratulacje!"), exit_program()

    if "niemiecki" in typed_lang_study:
        while word_list:
            for pair_word in word_list.copy():
                random.shuffle(word_list)
                pl_word = pair_word["pl"]
                de_word = pair_word["de"]
                answer = input(f"Tłumaczenie słowa '{de_word}' brzmi: ").lower()
                if answer == pl_word:
                    word_list.remove(pair_word)
                    score += 1
                    print(f"Twój aktualny wynik {score} z {total_points} punktów")
                elif answer == "exit program":
                    exit_program()
                else:
                    print(f"Poprawne słowo '{pl_word}'")
        return print("Wszystkie słowa poprawnie przetłumaczone, gratulacje!"), exit_program()
    return None

def eng_lang():
    """Shuffling and printing pair of words to print, scoring - ONLY LANGUAGE ENGLISH"""
    score = 0
    total_points = len(word_list)
    if "polish" in typed_lang_study:
        while word_list:
            for pair_word in word_list.copy():
                random.shuffle(word_list)
                pl_word = pair_word["pl"]
                eng_word = pair_word["eng"]
                answer = input(f"The translate for word '{pl_word}' is: ").lower()
                if answer == eng_word:
                    word_list.remove(pair_word)
                    score += 1
                    print(f"Your actual score {score} out of {total_points} points")
                elif answer == "exit program":
                    exit_program()
                else:
                    print(f"Proper word: '{eng_word}'")
        return print("All words translated correctly, congratulations!"), exit_program()

    if "german" in typed_lang_study:
        while word_list:
            for pair_word in word_list.copy():
                random.shuffle(word_list)
                eng_word = pair_word["eng"]
                de_word = pair_word["de"]
                answer = input(f"The translate for word '{de_word}' is: ").lower()
                if answer == pl_word:
                    word_list.remove(pair_word)
                    score += 1
                    print(f"Your actual score {score} out of {total_points} points")
                elif answer == "exit program":
                    exit_program()
                else:
                    print(f"Proper word: '{eng_word}'")
        return print("All words translated correctly, congratulations!"), exit_program()
    return None

def de_lang():
    """Shuffling and printing pair of words to print, scoring - ONLY LANGUAGE GERMAN"""
    score = 0
    total_points = len(word_list)
    if "polnisch" in typed_lang_study:
        while word_list:
            for pair_word in word_list.copy():
                random.shuffle(word_list)
                pl_word = pair_word["pl"]
                de_word = pair_word["de"]
                answer = input(f"Die Übersetzung des Wortes '{pl_word}' lautet: ").lower()
                if answer == de_word:
                    word_list.remove(pair_word)
                    score += 1
                    print(f"Ihr aktueller Punktestand beträgt {score} von {total_points} Punkten")
                elif answer == "exit program":
                    exit_program()
                else:
                    print(f"Richtiges Wort '{de_word}'")
        return print("Alle Wörter richtig übersetzt, Glückwunsch!"), exit_program()

    if "englisch" in typed_lang_study:
        while word_list:
            for pair_word in word_list.copy():
                random.shuffle(word_list)
                eng_word = pair_word["eng"]
                de_word = pair_word["de"]
                answer = input(f"Die Übersetzung des Wortes '{eng_word}' lautet: ").lower()
                if answer == de_word:
                    word_list.remove(pair_word)
                    score += 1
                    print(f"Ihr aktueller Punktestand beträgt {score} von {total_points} Punkten")
                elif answer == "exit program":
                    exit_program()
                else:
                    print(f"Richtiges Wort '{de_word}'")
        return print("Alle Wörter richtig übersetzt, Glückwunsch!"), exit_program()
    return None

if __name__ == "__main__":
    main()
