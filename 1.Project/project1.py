import sys
import csv

def main():

    check_sys_arg()
    after = []

    try:
        with open(sys.argv[1], "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                after.append({"first_name": row["first_name"], "last_name": row["last_name"], "email": row["email"]})
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")

    with open(sys.argv[2], "w") as csvfile2:
        after_writer = csv.DictWriter(csvfile2, fieldnames =["First_name", "Last_name", "Email"])
        after_writer.writerow({"First_name": "Imie Klienta", "Last_name": "Nazwisko Klienta", "Email": "Email Klienta"})
        for row in after:
            after_writer.writerow({"First_name": row["first_name"], "Last_name": row["last_name"], "Email": row["email"]})


def check_sys_arg():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not CSV file")




if __name__ == "__main__":
    main()
