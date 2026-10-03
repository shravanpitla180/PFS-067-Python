'''
#Inheritance 
#It is a process of acquring properties from parent class to child class.

#Types of Inheritance
#1. Single Inheritance
# One parent --> One child
#2. Multiple Inheritance
#One child --> Multiple parents
#Multi-level Inheritance
#3. Inheritance happens across multiple levels.
#GRandParent --> parent --> child
#4. Hierarchial Inheritance
#One parent --> Multiple childern
#5. Hybrid Inheritance
#Combination of two or more types of Inheritance
#6.Super Method
#In python,super() is used to access the functions of the parent class.
#7. Super() with constructor
'''


#1. Single Inheritance
# One parent --> One child
#Parent class
class Animal:
    def eat(self):
        print("Animal eats")

#Child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

l = Dog()
l.eat()
l.bark()


#2.Multiple Inheritance
#One child --> Multiple parents

class Father:
    def father_properties(self):
        print("Father's property")
class mother:
    def mother_properties(self):
        print("Mother's property")

class child(Father,mother):
    def child_properties(self):
        print("child's property")
c = child()
c.father_properties()
c.mother_properties()
c.child_properties()

#3. Multi-level Inheritance
#Inheritance happens across multiple levels.
#GRandParent --> parent --> child
class Grandparent:
    def Grandparent_house(self):
        print("Grandparent's house")
class parent(Grandparent):
    def parent_car(self):
        print("Parent's car")
class child(parent):
    def child_bike(self):
        print("child's bike")
c=child()
c.Grandparent_house()
c.parent_car()
c.child_bike()


#4. Hierarchial Inheritance
#One parent --> Multiple childern
class Animal:
    def eat(self):
        print("Animal eats")
class Dog(Animal):
    def bark(self):
        print("Dog barks")
class cat(Animal):
    def meow(self):
        print("cat meow")
class rat(Animal):
    def kich(self):
        print("rat kich")
d=Dog()
c=cat()
r=rat()
d.eat()
d.bark()
c.eat()
c.meow()
r.eat()
r.kich()


#5. Hybrid Inheritance
#Combination of two or more types of Inheritance

class A:
    def method_A(self):
        print("method of class A")
class B(A):
    def method_B(self):
        print("method of class B")
class C(A):
    def method_c(self):
        print("method of class c")
class D(B, C):
    def method_d(self):
        print("method of class D")
obj = D()
obj.method_A()
obj.method_B()
obj.method_c()
obj.method_d()

#6. Super Method
#In python,super() is used to access the functions of the parent class.


class  Parent:
    def show(self):
        print("parent method")
class child(Parent):
    def show(self):
        super().show()
        print("child method")
c = child()
c.show()

#7. Super() with constructor
class Person:
    def __init__(self,name):
        self.name = name
class student(Person):
    def __init__(self,name,age):
        super().__init__(name)
        self.age = age
s = student("shravan",21)
print(s.name)
print(s.age)
