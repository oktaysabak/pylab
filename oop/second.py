# %% inheritance/miras  ornegi


class Animal:  # parent class
    """ 
    En ustte bir sinif var ve bundan tureyen siniflar var. Turettigin siniflar turetilen sinifin ozelliklerini aynen alir.
    """

    def __init__(self, name):
        self.name = name
        print(f"{self.name} is created")

    def walk(self):
        print(f"{self.name} walks")

    def run(self):
        print(f"{self.name} runs")


class Monkey(Animal):  # child class
    def __init__(self, name):
        super().__init__(name)  # parent classin init metodunu iceri aktariyor

    def climb(self):
        print(f"{self.name} climb")


maymus = Monkey("monkey")
maymus.walk()
maymus.run()
maymus.climb()

# %% abstract / soyut class

from abc import ABC, abstractmethod


class Hayvan(ABC):
    """ 
    soyut sinif olusturmanin amaci kullanilmasi gereken ozellikler, metodlarin sablon seklinde hazirlanmasidir.
    olustur sinifi digerleri de bu metodlari mecbur kullanacak, sonra kendileri istedigi gibi takilsin
    """

    @abstractmethod  # bu metodlar child classta kullanilmak zorunda bro
    def walk(self):
        pass

    @abstractmethod
    def run(self):
        pass  # bu metodlar child classta kullanilmak zorunda bro


class Kus(Hayvan):
    def __init__(self):
        print("i came from abstract class")

    def walk(self):
        print("bird walk")

    def run(self):
        print("bird run")


kus = Kus()
# h = Hayvan() seklinde asla olusturamazsin, abstract classlarda abstract siniftan object olusturamazsin
