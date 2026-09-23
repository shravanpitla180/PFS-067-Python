# FUNCTION:-
# -simple block of code to do particular task
# why do we need functions:- to avoid repitation of code
# we have original implementation in functions

# Function syntax
# def function_name(parameter):
#     function body
#function creation
def greet():          #-greet()-function name
    print("Hello")    #-function body
greet()               #-function calling

def greet():
    return "world"
print(greet())

#user defined functions

#Types of Functions
# Type 1.no Parameters - m0 return value
#ex:-
def greet():
    print("hello sir")
greet()

#Type 2.Parameters,but no return value
def greet(name):         #name is my parameter
    print("Hello", name)
greet("shravan")

#Type 3.no parameter,but has return value
def get_number():
    return 100             #100 is my return value
result=get_number()
print(result)

#Type 4. Parmeters and return value
def add(a,b):       # a,b are my parameters
    return a+b      # a + b is my return value
result=add(2,3)     # 2 , 3 are arguments
print(result)  

#result-gives the result back to program

#returning multiple values
def calc(a,b):
    add=a+b
    sub=a-b
    return add,sub
x,y=calc(5,6)
print(x)
print(y)

#positional Arguments
#Arguments are matched based on their positions
def student(name, age):
    print("Name:",name)
    print("Age:",age)
student("shravan",21)


#keyword Arguments
def student(name, age):
    print(name)
    print(age)
student(age=21,name="shravan")

#Default Arguments
def function(name="shravan",age=23):    #giving values in parameters
    print("Hello",name,age)
function()

#variable - Lenght Arguments(*args)
def add(*numbers):      #*args -It collects multiple positional arguments into a tuple
    total=0
    for num in numbers:
        total += num
    return total
print(add(10,20,30,40,50))
print(add(1,5,2,3,4,6,7,8,9,9,7,8))

#keyword variable - length Arguments(**kwargs)

#Accepts multiple keyword arguments             #**kwargs --> Dictionary

def student_details(**details):
    print(details)
student_details(
    name="shravan",
    age=21,
    city="HYD"
)

#combination od both *args & **kwargs
def example(*args,**kwargs):
    print(args)
    print(kwargs)
example(10,20,30,40,name="shravan",age=21)

# scope=it is a region of a particular program where a variable can be accessed
#  2-Types
# 1)Local Scope
# 2)Global Scope

# --> 1) Local Scope
def display():
    name="shravan"
    age=21
    print(name)
    print(age)
display()
#an error can be raised if want to print the name outside the function after display()

#Different functions can have variables with same name
def first():
    x=30
    print(x)

def second():
    x=50
    print(x)

first()
second()

# Global Scope-->Variable declare outside the function has global scope
name="shravan"
age=21
def function():
    name="Ajay"
    print(name)
    print(age)
function()
print(name)
#No error can be raised if want to print the name outside the function after display()

x=100
def display():
    global x
    x=200
print(x)            #print outside value ex:-100      
display()
print(x)            #print inside value ex:-200


# Pass by value and pass by reference
def display(x):
    x=20
a=10
display(a)
print(a)

# Pass by value-->A copy of the value is passed to the function,changes made inside the function ,do not affect the original value
def change(x):                          #a-->10      
    x=20                                #calling the function change(a)
    print("Inside function: ",x)        #object
a=10                                    #x=20
change(a)                               #a-->10 x-->10
print("outside function: ",a)           #After x=20
                                        #a-->10 x-20

def add_10(x):
    x+=10
    print("Inside function: ",x)
num=50
add_10(num)
print("outside function: ",num)


#Pass by reference-->
def add_elements(data):
    data.append(40)
values=[10,20,30]
add_elements(values)
print(values)

#Recursion-->Function calling itself

def count_down(n):
    #Base case
    if n==0:
        return
    #Recursive case
    print(n)
    count_down(n-1)
count_down(5)


#Factorial ofa number using recursion
def fact(n):
    #Base case
    if n<=1:
        return 1
    #Recursive case
    return n * fact(n-1)
print(fact(6))

#fibanocci series using recursion


def fibanocci(n):
    if n<=1:
        return n
    return fibanocci(n-1)+fibanocci(n-2)
fib=5
for i in range(fib):
    print(fibanocci(i),end=" ")
