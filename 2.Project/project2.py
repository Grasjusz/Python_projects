"""Importing"""
import random
import sys


language_list = ["angielski", "niemiecki", "polish", "german", "polnisch", "englisch"]
word_list = []
typed_lang = []
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
            print("You have to choose between 3 levels, type: l1, l2 or l3")
            continue
        else:
            break

    pol_lang()

def check_language(language):
    """check chosen language and run proper"""
    if language == "polski":
        language_level = "Jakiego języka chcesz się uczyć? angielski lub niemiecki?: "
        return language_level
    if language == "english":
        language_level = "Which language would you like to learn? polish or german?: "
        return language_level
    if language == "deutsch":
        language_level = "Welches Sprache möchtest du lernen? polnisch oder englisch?: "
        return language_level
    if language == "exit program":
        exit_program()
    return None

def chosen_lang(learn_lang):
    """Checking and choosing proper file with words and translations"""
    if learn_lang in language_list:
        typed_lang.append(learn_lang)
        file_level = "test.csv"
        return file_level, typed_lang
    if learn_lang == "exit program":
        exit_program()
    return None

def pol_lang():
    """Shuffling and printing pair of words to print, scoring - ONLY LANGUAGES POLISH"""
    score = 0
    total_points = len(word_list)
    if "angielski" in typed_lang:
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
                    print(f"Poprawne słowo {pl_word}")
        return print("Wszystkie słowa poprawnie przetłumaczone, gratulacje!"), exit_program()

    if "niemiecki" in typed_lang:
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
                    print(f"Poprawne słowo {pl_word}")
        return print("Wszystkie słowa poprawnie przetłumaczone, gratulacje!"), exit_program()
    return None


def exit_program():
    """Exit program function"""
    print("Exiting the program...")
    sys.exit(0)

if __name__ == "__main__":
    main()