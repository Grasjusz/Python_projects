"""Importing"""


class Client:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"{self.name}"

    def client_name(self):
        name = self.split()
        return name

def main():
    client = client_name_fun()
    print(f"{client}")

def client_name_fun():
    client_name = input("Imię i nazwisko klienta: ")
    return Client.client_name(client_name)

if __name__ == "__main__":
    main()