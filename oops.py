
#oop: object oriented program
'''
it is a programmig apporach where we organize pur program around objects rather than only fucntions and variables.

student:
data: name,age,marks,roll_no.
behaviour: study(),attend_classes(),wirte_exam,display_details.
in oops, we combine data + behaviour into one object.

class: it is a blueprint or template to create an objects.

object: it is an instance of class. (actual thing created from blueprint).

#Attributes: properties of objects. attributes are data/properties associated wih an object.
#mthods: methods are nothing but functions which are created inside the class.
method only belongs to class.

#constructor: it is method which runs automatically when object is created. it is defined by "_init_()"
self represents current object.
'''

class student:
    def __init__(self,name,age,marks):   #constructor;  here name,age and amrks are attributes.
        self.name=name
        self.age=age
        self.marks=marks
        print(name)
        print(age)
        print(marks)
    def study(self):   #method
        print("Student is studying")
        
stud = student("shravan", 21, 69)
stud.study()
print(stud.name)
print(stud.age)
print(stud.marks)


#Encapsuation:
# Encapsulation means bunding the data and methods together inside a
# class and controlling how that data is accessed and modified
#EG:-
class BankAccount:
    def __init__(self, balance):
        self._balance = balance
    def deposite(self, amount):
        if amount>0:
            self._balance += amount
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
    def get_balance(self):
        return self._balance
balance= BankAccount(50000)
balance.deposite(10000)
balance.withdraw(5000)
print(balance.get_balance())
#Double underscore(__) indicates a private - like attrribute in python through name managing.


#Getter and setter concept

# Private Data
# Getter --> Read Data       
#Setter --> Modify data safely

class student:
    def __init__(self,marks):
        self.__marks = marks
    def get_marks(self):
        return self.__marks
    def set_marks(self, marks):
        if 0<=marks<=100:
            self.__marks = marks
        else:
            print("Invalid marks")
student1 = student(80)
print(student1.get_marks())
student1.set_marks(90)
print(student1.get_marks())