# from abc import *
# class Vehicle(ABC):
#     @abstractmethod
#     def wheels(self):
#         pass
# class Bus(Vehicle):
#     pass
# b=Bus()

from abc import *
class Vehicle(ABC):
    @abstractmethod
    def wheels(self):
        pass
class Bus(Vehicle):
    def wheels(self):
        return 7
class Auto(Vehicle):
    def wheels(self):
        return 4
b=Bus()
a=Auto()
print(b.wheels())
print(a.wheels())
