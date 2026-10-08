#indexing
name="codegnan"
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])
print(name[7])

print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])
print(name[-8])

#complex number
a=3+4j
print(a.real)
print(a.imag)

#lists
shravan = [90,70,80,77,96]
print(shravan)

#list_name[index]=new_value
shravan[0]=100
print(shravan)

student=[10, "shravan" ,"Hyderabad",7.27]
print(student)

#adding elements
#append() -add the elements
student.append(200)
print(student)
#extend() -to join the elements
a=[10 ,20 ,30]
b=[12 ,40 ,33]
a.extend(b)
print(a)
#used to delete the ending element
a.pop()
print(a)
#used to remove a particular number
a.remove(40)
print(a)


#string
city="hyderabad is capital of telangana"
place='hyderabad is capital of telangana'
print(city == place)

print(city)
print(place)

word="python"
print(word[-6:-1])

#replace
word="python" 
result=word.replace("h","")
print(result)
print(word)

text="python"
for char in text:
    if char=="h":
        continue
print(char,end="")

#concatination
first_name="shravan"
last_name="kumar"
name=first_name+last_name
print(name)

a="shravan"  #isalpha()-contains all alphabets from A-Z,a-z
b="1807"     #isdigit()-contains all digits expect decimals
c="shravan kumar" #isalnum()-contains combimation of alphabets & digits
print(a.isalpha())
print(b.isdigit())
print(c.isalnum())

name="shravan"
print(name)
print(type(name))
#indexing
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

#negative indexing
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])

#slicing
print(name[:5])
print(name[1:])
print(name[0:7:2])

#concatinate
list1="code"
list2="gnan"
company=list1+list2
print(company)

#string repeat
string="codegnan","spilt"
result=(string*3)
print(result)

#compare two strings
a="shravan"
b="saikiran"
print(a==b)
#index to find position
a="codegnan"
print(a.index("g"))

#count()
name="shravan"
print(name.count("a"))
print(name.count("s"))

#string into upper(),lower(),title()
name="shravan is from medak"
print(name.upper())
print(name.lower())
print(name.title())
#capitalize
print(name.capitalize())
#removing unwanted spaces strip(),lstrip(),rstrip()
abc="          shravan          "
print(abc.strip())
print(abc.lstrip())
print(abc.rstrip())
#replace part of string using replace()
str="shravan"
result=str.replace("h","+")
print(result)
#split a string using split()
lang="java,pyhton,flask"
a=lang.split(",")
print(a)
#join()
list="python","java","sql"
a="-".join(list)
print(a)
#string contains isalpha()
text="shravan"
print(text.isalpha())
text="shra1"
print(text.isalpha())
#isalnum()
text="shravan"
print(text.isalnum())
text="shra1"
print(text.isalnum())
#isdigit()
text="1807"
print(text.isdigit())
#isspace()
text="shravan kumar"
print(text.isspace())
#islower
text="shravan"
print(text.islower())
text="Shravan"
print(text.islower())
#isupper()
text="Shravan"
print(text.isupper())
text="SHRAVAN"
print(text.isupper())
#istitle()
text="Shravan is from medak"
print(text.istitle())
text="Shravan Is From Medak"
print(text.istitle())
#startswith()
name="shravan is a software engineer"
a=name.startswith("shravan")
print(a)
name="shravan is a software engineer"
a=name.startswith("software")
print(a)
name="shravan is a software engineer"
print(name.startswith("shravan"))
#endswith()
name="shravan is a software engineer"
a=name.endswith("engineer")
print(a)
name="shravan is a software engineer"
print(name.endswith("shravan"))