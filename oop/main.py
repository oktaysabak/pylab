import time
import tqdm


class Employee:  # icrisindeki obje classina ait bir nesne, zorunlu degil
    # ozellikleri burada tutuyoruz (attribute)
    name = "oktay"
    age = 28
    address = "siirt"
    company = "startech"
    # davranissal kavramlar da tutulabilir (behaviour) kod_yaz, kitap_okuma
    @staticmethod
    def kod_yaz():
        print("kod yaziyor")


# %%
class Coder:
    # attributes
    name = ""
    surname = ""
    skills = []

    # methods
    def set_name(self, new_name):
        self.name = new_name

    def set_surname(self, new_surname):
        self.surname = new_surname

    def add_skill(self, skill):
        self.skills.append(skill)

    def get_skills(self):
        return self.skills

    def get_fullname(self):
        return self.name + " " + self.surname


# functions
def get_fullname(name, surname):
    print(name.upper() + " " + surname.upper())


# %% initializer yapilandirici method


class Animal:
    def __init__(self, name="animal"):
        self.name = name

    def set_type(self, name):
        self.name = name

    def get_type(self):
        return self.name


# %%
class Calculator:
    def __init__(self, number1: int, number2: int):
        try:
            self.first_number = int(number1)
            self.second_number = int(number2)
        except TypeError:
            print("You should create object with decimal values...")

    def add(self):
        return self.first_number + self.second_number

    def minus(self):
        return self.first_number - self.second_number

    def multiply(self):
        return self.first_number * self.second_number

    def divide(self):
        try:
            return self.first_number / self.second_number
        except ZeroDivisionError:
            return "you can't divide with 0...."

    def results(self):
        for _ in tqdm.tqdm(range(4)):  # progressbar ekledim
            time.sleep(0.2)
            pass
        print(f"{self.first_number} + {self.second_number} = {self.add()}")
        print(f"{self.first_number} - {self.second_number} = {self.minus()}")
        print(f"{self.first_number} * {self.second_number} = {self.multiply()}")
        print(f"{self.first_number} / {self.second_number} = {self.divide()}")


# %% encapsulation
class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.__title = title
        self.__author = author
        self.__isbn = isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def show(self):
        print(f"{self.get_title()} - {self.get_author()} - {self.get_isbn()}")


if __name__ == "__main__":
    NEW_USER = Employee()
    print(NEW_USER.name)
    print(NEW_USER.age)
    print(NEW_USER.address)
    NEW_USER.kod_yaz()
    NEW_USER.address = "malatya"
    print("new address", NEW_USER.address)  # ozelliklere erisip degistirebiliyoruz
    for _ in tqdm.tqdm(range(10)):  # progressbar ekledim
        time.sleep(0.1)
        pass
    OKTAY = Coder()
    OKTAY.set_name("oktay")
    OKTAY.set_surname("sabak")
    OKTAY.add_skill("python")
    OKTAY.add_skill("c")
    OKTAY.add_skill("django")
    print(OKTAY.get_fullname())
    print(OKTAY.get_skills())
    get_fullname(OKTAY.name, OKTAY.surname)
    for _ in tqdm.tqdm(range(10)):  # progressbar ekledim
        time.sleep(0.1)
        pass
    ANIMAL = Animal()
    print("this is", ANIMAL.get_type())
    ANIMAL.set_type("dog")
    print("this animal is", ANIMAL.get_type())
    for _ in tqdm.tqdm(range(10)):  # progressbar ekledim
        time.sleep(0.1)
        pass
    print("let's calculate 5 times!")
    print("--------------------------")
    for i in range(5):
        try:
            first = input("give first number: ")
            second = input("give second number:")
            print("calculating...")
            calc = Calculator(first, second)
            calc.results()
        except ValueError:
            print(" LoL ")
    print("let's add books to storage!")
    print("--------------------------")
    BOOKS = []
    for i in range(4):
        book_title = input("book name: ")
        book_author = input("book author: ")
        book_isbn = input("book isbn number: ")
        b = Book(book_title, book_author, book_isbn)
        BOOKS.append(b)
    for book in BOOKS:
        book.show()
