# Unlimited arguments

# def add(*args):
#     total = 0
#     for n in args:
#         total += n
#     return total

# print(add(1, 2, 3))

# Unlimited keyword arguments

def calculate(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["multiply"]
    return n

print(calculate(2, add = 3, multiply = 5))

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="nissan", model="gtr")