#1.Identify number whether the number belongs to +ve or -ve or zero


# num=int(input("enter the number"))
# if num>0:
#     print("positive")
# elif num<0:
#     print("negative")
# else:
#     print("zero")

#2.even or odd number


# digit=int(input("enter the number"))
# if digit % 2==0:
#     print("even")
# elif digit%2!=0:
#     print("odd")
# else:
#     print("zero")

#3.largest of 2 numbers


# A=int(input("enter value of A: "))
# B=int(input("enter value of B: "))
# if A>B:
#     print("A is greater than B")
# elif B>A:
#     print("B is greater than A")
# else:
#     print("A,B are equal")

# #4.college Admission
# marks=int(input("enter marks: "))
# Entrance=input("Did you pass entrance exam? (yes,no): ")

# if marks>=70 and Entrance=="yes":
#     print("eligiable")
# elif marks>70 and Entrance=="no":
#     print("not eligible")
# else:
#     print("failed")

#####username=admin
#password=password123

# username=input()
# password=int(input())
# if username=="shravan" and password=="1232":
#     print("login successful")
# else:
#     print("login unsuccessful")

# ###under 18  - too young to drive
# 18+ but no license - valid license required
# 18+ with license - you can drive

# age=int(input("enter age: "))
# license=input("(yes/no): ")

# if age>=18 and license=="yes":
#     print("you can drive")
# elif age>=18 and license=="no":
#     print("valid license is required")
# else:
#     print("too young to drive")

##### movie ticket pricing
##### Below 5 - free
##### 5-12 =100
##### 13 - 50=200
##### 60 and above = 120

# age=int(input("enter age: "))


# if age<5:
#     print("ticket is free")
# elif age>=5 and age <=12:
#     print("ticket price is 100")
# elif age>=13 and age<=50:
#     print("ticket price is 200")
# else:
#     print("ticket price is 120")

#####leap year

# year=int(input("enter year"))

# if year %4==0 and year %100!=0 and year%400==0:
#     print("leap year")
# else:
#     print("not a leap year")


#employee management system
#performance is > 90 and exp > 5 = 20% hike 
#performance is > 90 and exp < 5 = 10% hike 
#performance is > 80 =10% hike 
#performance is > 70 =5% hike 

emp=int(input("enter performance: "))
exp=int(input("enter experience: "))

if emp>90 and exp >=5:
    print("expected hike is 20%")
elif emp>90 and exp <5:
    print("hike is 10%")
elif emp>80:
    print("hike 10%")
elif emp>70:
    print("hike 5%")
else:
    print("no hike")

    





    if emp>80:
        print("hike is 10%")
    elif emp > 70:
        print("hike is 5%")


