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