import random
import sys

def main():

    word_list = []

    while True:
        level = input("Which level would you try? (type: 'l1'(easy), 'l2'(medium) or 'l3'(hard)) type 'exit program' to exit: ").lower()
        try:
            file_level = open(check_lvl(level), "r", encoding="utf-8")
            for line in file_level:
                line = line.lower()
                eng, pl = line.rstrip().split(",")
                word_list.append({"eng":eng, "pl":pl})
        except (NameError, TypeError):
            print("You have to choose between 3 levels, type: l1, l2 or l3")
            continue
        else:
            break

#Shuffling and printing pair of the words to print
    for pair_word in word_list:
        random.shuffle(word_list)
        eng_word = pair_word["eng"]
        pl_word = pair_word["pl"]
        answer = input(f"Word translation for {eng_word} is: ").lower()
        if answer == pl_word:
            pass
        elif answer == "exit program":
            exit_program()
        else:
            print(f"Correct word: {pl_word}")

#Checking and choosing proper file with words
def check_lvl(level):
    if level == "l1":
        file_level = "level1.csv"
        return file_level
    elif level == "l2":
        file_level = "level2.csv"
        return file_level
    elif level == "l3":
        file_level = "level3.csv"
        return file_level
    elif level == "exit program":
        exit_program()

def exit_program():
    print("Exiting the program...")
    sys.exit(0)

if __name__ == "__main__":
    main()