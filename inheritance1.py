class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def eatndrink(self):
        print("Eat briyani and drink")
class Employee(Person):
    def __init__(self,name,age,eno,esal):
        super().__init__(name,age)
        self.eno=eno
        self.esal=esal
    def work(self):
        print("Coding in python")
    def empinfo(self):
        print("Emp name:",self.name)
        print("Emp age:",self.age)
        print("Emp number:",self.eno)
        print("Emp salary:",self.esal)
e=Employee("Dharshan",20,45,50000)
e.eatndrink()
e.work()
e.empinfo()
