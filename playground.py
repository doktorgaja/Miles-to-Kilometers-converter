# UNLIMITED ARGUMENTS *args
# def add(*args):
# obavezno zvezdica mora
# dozvoljava neogranicenu upotrebu argumenata
# dakle za svako n u argsu ispisi n
# imamo deklarisane vec n1 i n2 ili
# mozemo koristiti koliko god zelimo argumenata jer
# svi oni potapdaju pod n
#   for n in args:
#       print(n)
# add(n1=5, n2=3)
# add(3, 5, 7, 9)

def add(*args):
    print(args[0])

    sum = 0
    for n in args:
        sum += n
    return sum
print(add(3, 5, 6))

# ne mora se samo pristupiti pozicionom argumentu preko broja vec i preko keyworda

def calculate(n, **kwargs):
    # pravi dictionary kad se u konzoli pozove
    # ima keyword i value
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
# ako ne stavimo nista u zagrade kao vrednost onda uzima default vrednost tj none
print(my_car.model)
