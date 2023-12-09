"""Importing"""
import random
import sys

def main():
    """Main program"""

    word_list = []
    score = 0
    while True:
        language = input("Choose your language: polski, english or deutsch: ").lower()
        level = input(check_language(language)).lower()
        try:
            with open(check_lvl(level), "r", encoding="utf-8") as file_level:
                for line in file_level:
                    line = line.lower()
                    eng, pl = line.rstrip().split(",")
                    word_list.append({"eng":eng, "pl":pl})
        except (NameError, TypeError):
            print("You have to choose between 3 levels, type: l1, l2 or l3")
            continue
        else:
            break

#Shuffling and printing pair of words to print, scoring.
    while word_list:
        total_points = len(word_list)
        for pair_word in word_list.copy():
            random.shuffle(word_list)
            eng_word = pair_word["eng"]
            pl_word = pair_word["pl"]
            answer = input(f"Word translation for {eng_word} is: ").lower()
            if answer == pl_word:
                word_list.remove(pair_word)
                score += 1
                print(f"You actual score is {score} of total {total_points} points")
            elif answer == "exit program":
                exit_program()
            else:
                print(f"Correct word: {pl_word}")
    return print("All words translated, congratulations!"), exit_program()


def check_language(language):
    if language == "polish":
        language_level = "Który poziom byś wypróbował? (wpisz: 'l1' (łatwy), 'l2' (średni) lub 'l3' (trudny)) wpisz 'exit program', aby wyjść: "
        return language_level
    if language == "english":
        language_level = "Which level would you try? (type: 'l1'(easy), 'l2'(medium) or 'l3'(hard)) type 'exit program' to exit: "
        return language_level
    if language == "german":
        language_level = "Welches Level würdest du ausprobieren? (Typ: 'l1' (einfach), 'l2' (mittel) oder 'l3' (schwer)) Geben Sie 'exit program' ein, um zu beenden: "
        return language_level
    return None

def check_lvl(level):
    """Checking and choosing proper file with words and translations"""
    if level == "l1":
        file_level = "level1.csv"
        return file_level
    if level == "l2":
        file_level = "level2.csv"
        return file_level
    if level == "l3":
        file_level = "level3.csv"
        return file_level
    if level == "exit program":
        exit_program()
    return None

def exit_program():
    """Exit program function"""
    print("Exiting the program...")
    sys.exit(0)

if __name__ == "__main__":
    main()