# %% polymorphism cok sekilcilik :)
""" 
aslinda yapilan su: parent klasin var, ondan tureyen child classlar var. 
sen parent sinifinda kullandigin fonksiyonlari ayni sekilde child siniflarda kullaniyorsan 
ama farkli islemler yaptiriyorsan polimorfizm yapmis oluyorsun.
aslinda cogu zaman yapiyorsun da farkinda olmuyorsun.
"""
import time


class Staff:
    """ our company's staff base class """

    def __init__(self, name: str, surname: str, staff_number: str, payment: int):
        self.name = name
        self.surname = surname
        self.staff_number = staff_number
        self.payment = payment
        self.raise_rate = 0.1

    def raise_payment(self):
        self.payment += self.payment * self.raise_rate


class ComputerEngineer(Staff):
    """ company's computer engineers will create with this class """

    def __init__(self, name, surname, staff_number, payment):
        super().__init__(name, surname, staff_number, payment)
        self.raise_rate = 0.2

    def raise_payment(self):
        self.payment += self.payment * self.raise_rate


class SoftwareEngineer(Staff):
    """ company's software engineers will create with this class """

    def __init__(self, name, surname, staff_number, payment):
        super().__init__(name, surname, staff_number, payment)
        self.raise_rate = 0.3

    def raise_payment(self):
        self.payment += self.payment * self.raise_rate


staff = Staff("oktay", "sabak", "20426534789", 500)

computer_engineer = ComputerEngineer(
    staff.name, staff.surname, staff.staff_number, staff.payment
)
software_engineer = SoftwareEngineer(
    staff.name, staff.surname, staff.staff_number, staff.payment
)

print("staff payment: ", staff.payment)
print("---------")
print("computer engineer payment: ", computer_engineer.payment)
print("---------")
print("software engineer payment: ", software_engineer.payment)
print("---------")
print("staff base payment increasing....")
time.sleep(2)
staff.raise_payment()
print("staff payment: ", staff.payment)
print("---------")
print("computer engineerpayment increasing....")
time.sleep(2)
computer_engineer.raise_payment()
print("computer engineer payment: ", computer_engineer.payment)
print("---------")
print("software engineer payment increasing....")
time.sleep(2)
software_engineer.raise_payment()
print("software engineer payment: ", software_engineer.payment)
print("---------")
