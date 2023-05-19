'''
types of class relationships (inheritance):

association: general binary relationshio that describes an activity between 2 classes
(usually represented as a data field, i.e. a course that a teacher teaches and a student takes)

composition/aggregation: a class has an attribute that is an object of another class, a dependency
(helps with attributes that are more complicated, i.e. profit --> salary? bonus? tax?)

'''

#ex 1

class Salary():
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
    
    def getSalary(self):
        return self.pay + self.bonus

class Employee():
    def __init__(self, name, age, pay, bonus):
        self.salary = Salary(pay, bonus)
        self.name = name
        self.age = age
    
#ex 2

    