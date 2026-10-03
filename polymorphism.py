'''
Polymorphism = One name ,many forms
Poly - Many
Morphism - Forms

- In python, Polymorphism means same method, function or operator can behave differently depending on the object or data being used.
'''
class dog:
    def sound(self):
        print("Dog barks")
class cat:
    def sound(self):
        print("cat meows")
d=dog()
c=cat()
d.sound()
c.sound()


#Types of Polymorphism:

#1. Method Overloading
#2. Method Overriding
#3. Operator overloading

#Method Overriding:
# -->It occcurs when a child class provides  it's owm implementation that already exists in parent class.

class Animal:
    def sound(self):
        print("Animal makes sound")
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("cat meows")
d=Dog()
c=Cat()
d.sound()
c.sound()

#Method Overloading:
# -->Having multiple methods with same name but  different parametersin the same class

class Calculator:
    def add(self,a,b):
        return a+b
    def add(self,a,b,c=0):
        return a+b+c
calc=Calculator()
print(calc.add(4,5))    #a,b machine c=0 automatically
print(calc.add(8,5,6))

# Using *args 
class calc:
    def add(self,*args):
        return sum(args)
c = calc()
print(c.add(10,20))
print(c.add(10,20,30))
print(c.add(10,20,30,40))
print(c.add(10,20,30,40,50))
print(c.add(10,20,30,40,50,60))


print(10+20)
print("Hello" + "world")

#Operator Overloading:It means giving operators such as + ,- ,* ,/ ,==,etc.special behaviour for our own objects
class point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self,other):
        return point(
            self.x + other.x,
            self.y + other.y
        )
p1 = point(10,20)
p2 = point(30,40)
p3= p1 +p2      #p1.__add__(p2) p3.x = 10+30=40,20+40=60.
print(p3.x)
print(p3.y)

class student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def __eq__(self,other):
        return self.marks == other.marks
s1 = student("shravan",96)
s2 = student("sai",96)
print(s1 == s2)


