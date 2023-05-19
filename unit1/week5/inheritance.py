'''
inheritance allows us to inherit attributes and/or methods from the base/parent class
- child class inherits the properties from the parent class


types of inheritance:

single (B inherits from A)
B --> A

multilevel
C --> B --> A

hierarchical
C --> A <-- B

multiple
A <-- C --> B
'''
from __future__ import absolute_import
from enum import auto


class A:
    def __init__(self):
        print("class A")

    def print2(self):
        print("class A 2")

#put the name of parent class in parentheses
class B(A):
    def __init__(self):
        #by default, it does not call the constructor from the parent class
        A.__init__(self) #inherit function (pass in the parameter of self)
        super().print2() #you can also use super() instead of obj name
        print("class B")

b = B()
b.print2() #you can call functions from parent class from child obj


#from uml diagram

class automobile:

    __make = ""
    __model = 0
    __mileage = 0
    __price = 0.0

    def __init__(self, make, model, mileage, price):
        self.__make = make
        self.__model = model
        self.__mileage = mileage
        self.__price = price
    
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model
    
    def set_mileage(self, mileage):
        self.__mileage = mileage
    
    def set_price(self, price):
        self.__price = price
    
    def get_make(self):
        return "Make: " + str(self.__make)
    
    def get_model(self):
        return "Model: " + str(self.__model)

    def get_mileage(self):
        return "Mileage: " + str(self.__mileage)

    def get_price(self):
        return "Price: " + str(self.__price)

class car(automobile):
    __doors = 0

    def __init__(self, make, model, mileage, price, doors):
        self.__doors = doors
        super().__init__(make, model, mileage, price)
    
    def set_doors(self, doors):
        self.__doors = doors
    
    def get_doors(self):
        return "Number of doors: " + str(self.__doors)

class truck(automobile):
    __drive_type = ""

    def __init__(self, make, model, mileage, price, drive_type):
        self.__drive_type = drive_type
        super().__init__(make, model, mileage, price)
    
    def set_drive_type(self, drive_type):
        self.__drive_type = drive_type
    
    def get_drive_type(self):
        return "Drive Type: " + str(self.__drive_type)

class SUV(automobile):
    __pass_cap = 0

    def __init__(self, make, model, mileage, price, pass_cap):
        self.__pass_cap = pass_cap
        super().__init__(make, model, mileage, price)

    def set_pass_cap(self, pass_cap):
        self.__pass_cap = pass_cap
    
    def get_pass_cap(self):
        return "Passenger Capacity: " + str(self.__pass_cap)

def main():
    #make the objects
    car1 = car("BMW", 2001, 70000, 15000.0, 4)
    truck1 = truck("Toyota", 2002, 40000, 12000.0, "4WD")
    suv1 = SUV("Volvo", 2000, 30000, 18500.0, 5)

    print("USED CAR INVENTORY", "================", sep="\n")

    #car
    print("The following car is in inventory:")
    print(
        car1.get_make(),
        car1.get_model(),
        car1.get_mileage(),
        car1.get_price(),
        car1.get_doors(),
        "",
        sep="\n"
    )
    #truck
    print("The following pickup truck is in inventory:")
    print(
        truck1.get_make(),
        truck1.get_model(),
        truck1.get_mileage(),
        truck1.get_price(),
        truck1.get_drive_type(),
        "",
        sep="\n"
    )

    #suv
    print("The following SUV is in inventory:")
    print(
        suv1.get_make(),
        suv1.get_model(),
        suv1.get_mileage(),
        suv1.get_price(),
        suv1.get_pass_cap(),
        "",
        sep="\n"
    )

main()