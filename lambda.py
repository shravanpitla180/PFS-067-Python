#Lambda function-->Anonymous function

# Anonyamous-- without name
# small anonymous functions 
# single line function


#lambda syntax
#lambda arguments : expression

#square function
# without lambda

def square(x):
    print(x*x)
square(5)

# with lambda
print("lambda with one parameter")
square =lambda x : x * x
print(square(3))

print("lambda with multiple parameters")
add=lambda x ,y : x+y
print(add(10,40))

add=lambda a,b,c,d : a+b+c+d
print(add(1,2,5,8))


sub=lambda a,b : a - b
print(sub(10,20))

# Lambda with if-else
print("Lambda with if-else")
check = lambda x: "even" if x%2==0 else "odd"
print(check(10))
print(check(3))

# when should we use lambda-->

# some techniques
# small functions temporarily,especially with :-map() ,filter() ,sorted() ,reduce().

# map():->It applies functions to every element of an iterable
# syntax:map(function,iterable)
print("map() function with lambda")
# example:-
nums=[1,2,3,4,5,6,7,8,9]
squares = list(map(lambda x :x*x,nums))
print(squares)

#map() without lambda
print("map() without lambda")
def square(x):
    return x*x
numbers=[1,2,3,4,5]
result=map(square,numbers)
print(list(result))


#Filter()-->It is used when we want to select only elements that statisy  condition

#syntax:-->filter(function,iteration)
print("displaying even numbers using filter()")
nums=[1,2,3,4,5,6,7,8]
result = filter(lambda x : x%2==0 , nums)
print(list(result))


print("displaying odd numbers using filter()")
nums=[1,2,3,4,5,6,7,8]
result = filter(lambda x : x%2!=0 , nums)
print(list(result))

#Reduce()-->It repeatedly applies a function to elements and reduces entire sequence to one final value

# from functools import reduce

print("displaying using reduce()")
from functools import reduce
numbers = [1,2,3,4,5]
result=reduce(lambda a, b : a + b,numbers)
print(result)

names=["shravan","puppy","ajay","rama"]
result=sorted(names,key=len)
print(result)

nums=[3,2,9,7,-6,-8,-9,21]
result=sorted(nums,key=abs)
print(result)

# sorted words by last character
names=["shravan","sairam","rajendra","avinash","chatan"]
result=sorted(names,key=lambda x:x[-1])
print(result)