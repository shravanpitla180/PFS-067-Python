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

