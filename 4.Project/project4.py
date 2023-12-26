import csv
import re


level = 0

def main():
     
    while True:
        try:
            level = 1
            name = name_func(input("What's your name?: "), level)
            level = 2
            second_name = name_func(input("What's your second name?: "), level)
            level = 3
            email = email_func(input("What's your email adress?: "), level)
            print("all answers saved!")
            break
        except:
            print("Ocurred error, try again")
            
    
    
    
    
    
def name_func(name, level):
    name_pattern = re.search(r"^(?=.*[a-zA-Z]{1,})(?=.*[\d]{0,})[a-zA-ZĄąĆćĘęŁłŃńÓóŚśŹźŻż]{3,15}$", name)
    if name_pattern:
        return True
    else:
        if level == 1:
            print("There is error in name")
            name = name_func(input("What's your name?: "), level)
        if level == 2:
            print("There is error in second name")
            name = name_func(input("What's your second name?: "), level)
        return None
        

    
def email_func(email, level):
    email_pattern = re.search(r"^((?!\.)[\w\-_.]*[^.])(@\w+)(\.\w+(\.\w+)?[^.\W])$", email)
    if email_pattern:
        return True
    else:
        if level == 3:
            print("There is error in email adress")
            email = email_func(input("What's your email adress?: "), level)
        return None
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    main()