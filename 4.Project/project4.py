"""Importing modules"""
import csv
import re


def main():
    """Main module running program."""

    while True:
        try:
            level = 1
            name = name_func(input("What's your name?: "), level)
            level = 2
            second_name = name_func(input("What's your second name?: "), level)
            level = 3
            email = email_func(input("What's your email adress?: "), level)
            details_list = [name, second_name, email]
            correct_func(input(f"""Are these details correct: {details_list}?
if yes, type 'Y' if no, type 'N' - process will start again: """), details_list)
            break
        except ValueError:
            print("Ocurred error, try again")

def name_func(name, level):
    """Checking if name, second name is proper - no digits etc allowed. Min 3 letters, Max 15 letters"""

    name_pattern = re.search(r"^(?=.*[a-zA-Z]{1,})(?=.*[\d]{0,})[a-zA-ZĄąĆćĘęŁłŃńÓóŚśŹźŻż]{3,15}$",
                             name)
    if name_pattern:
        return name
    else:
        if level == 1:
            print("There is error in name")
            name = name_func(input("What's your name?: "), level)
        if level == 2:
            print("There is error in second name")
            name = name_func(input("What's your second name?: "), level)
        return name

def email_func(email, level):
    """Checking if email is proper format."""

    email_pattern = re.search(r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$",
                              email)
    if email_pattern:
        return email
    else:
        if level == 3:
            print("There is error in email adress")
            email = email_func(input("What's your email adress?: "), level)
        return email

def correct_func(correct, details_list):
    """Checking if user input is to refullfilement or to save.
    If save - informations are saved to CSV file."""

    if correct in ["Y","y","Yes","yes"]:
        with open("4.Project/contacts.csv", "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(details_list)
            file.close()
            print("Saved!")
    if correct in ["N","n","No","no"]:
        return main()

if __name__ == "__main__":
    main()
