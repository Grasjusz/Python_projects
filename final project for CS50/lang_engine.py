"""Importing"""
import random
import sys

def main():
    pass

def exit_program():
    """Exit program function"""
    print("Exiting the program...")
    sys.exit(0)

def pol_lang(typed_lang_study, words):
    """Shuffling and printing pair of words to print, scoring - ONLY LANGUAGE POLISH"""
    score = 0
    word_list: list = words
    total_points = len(word_list)
    if "angielski" in typed_lang_study:
        while word_list:
            for pair_word in word_list:
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
            for pair_word in word_list:
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

def eng_lang(typed_lang_study, words):
    """Shuffling and printing pair of words to print, scoring - ONLY LANGUAGE ENGLISH"""
    score = 0
    word_list: list = words
    total_points = len(word_list)
    if "polish" in typed_lang_study:
        while word_list:
            for pair_word in word_list:
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
            for pair_word in word_list:
                random.shuffle(word_list)
                eng_word = pair_word["eng"]
                de_word = pair_word["de"]
                answer = input(f"The translate for word '{de_word}' is: ").lower()
                if answer == eng_word:
                    word_list.remove(pair_word)
                    score += 1
                    print(f"Your actual score {score} out of {total_points} points")
                elif answer == "exit program":
                    exit_program()
                else:
                    print(f"Proper word: '{eng_word}'")
        return print("All words translated correctly, congratulations!"), exit_program()
    return None

def de_lang(typed_lang_study, words):
    """Shuffling and printing pair of words to print, scoring - ONLY LANGUAGE GERMAN"""
    score = 0
    word_list: list = words
    total_points = len(word_list)
    if "polnisch" in typed_lang_study:
        while word_list:
            for pair_word in word_list:
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
            for pair_word in word_list:
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
