'''
Abstraction:-
-->It means hidding unnecessary implementation details and exposing only the required functionallity
'''

from abc import ABC, abstractmethod
#ABC called as Abstract Base Class
class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

#Animal says that every animal must provide a sound() method
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("cat meow")
dog = Dog()
dog.sound()
cat = Cat()
cat.sound()


from abc import ABC,abstractmethod

class payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass
class UPI(payment):
    def pay(self,amount):
        print("Paid",amount,"using UPI")
class CreditCard(payment):
    def pay(self,amount):
        print("Paid",amount,"using CreditCard")

upi = UPI()
card = CreditCard()
upi.pay(5000)
card.pay(10000)
