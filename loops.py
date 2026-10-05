#1) by using index
# for i in range(1,11):
#     print("hello")

# for i in range(1,11):
#     print(i)

# nums=[10,20,30,40,50,60]
# for i in range(0,6):
#     print(nums[i])

#2)by using value
# nums=[10,20,30,40,50,60]
# for num in nums:
#     print(num)

# li=[54,56,75,85,9,266,58,122,43,5,1,42,42,51,9,86,32]
# for num in li:
#     print(num)

#while loop
#syntax
# i=1
# while i <= 5:
#     print(i)
#     i+=1

#print even numbers from 1 to 10
# i=1
# while i<=10:
#     if(i%2==0):
#         print(i)
#         i+=1


# for loop
# for i in range(1,11):
#     if (i%2==0):
#         print(i)


# num=int(input("enter number: "))
# for i in range(1,11):
#     print(num*i)

# #finding number in a array without ,maths

# nums=[10,20,30,40,50]
# largest=nums[0]
# for num in nums:
#     if num>largest:
#         largest=num
# print(largest)

# nums=[10,20,30,40,50]
# smallest=nums[0]
# for num in nums:
#     if num<smallest:
#         smallest=num
# print(smallest)


# number=int(input("enter the num: "))
# print("palindrone"if(str(number)==str(number)[::-1]and len(str(number))>=3)else"Not a palindrome")


#write a python program to sum all the items in list
def list(ex):
    sum=0
    for i in ex:
        sum+=i
    return sum
print(list([1,2,3,4,6]))