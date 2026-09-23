#dictionary
student={
    "name":"shravan",
    "age":21,
    "place":"hyd"
}
print(student)
print(max(student))
print(min(student))
print(sorted(student))
#Access values using keys
print(student["name"])
print(student["age"])
print(student["place"])

#access values using get()
print(student.get("name"))
print(student.get("missing"))

#adding new key values pair
student["gpa"]=7.27
print(student)

#modify an existing value
student["age"]=23
print(student)

#add multiple key value pairs using update()
student.update({"mobile":6303401855,"city":"Ramayampet"})
print(student)

#remove element using pop()
student.pop("mobile")
print(student)

#remove last inserted pair of key:value 
student.popitem()
print(student)

# clear()
student.clear()
print(student)

# len()
student=len(student)
print(student)

#new dict
emply={
    "name":"shravan",
    "age":21,
    "city":"hyd",
    "mobile":6303401855,
    "salary":200000
}
print(emply)

# keys()
print(list(emply.keys()))

# values()
print(list(emply.values()))

#items()
print(list(emply.items()))

#copy()
print(emply.copy())

#create a dictionary using fromkeys()
keys=["a","b","c","d"]
value=dict.fromkeys(keys,2)
print(value)

#create data on your own data(id,name,email,cgpa,college),priint(all the key value pairs,modify email,cgpa
# college nmae in short form,sorted)
Details={
    "id" :3389,
    "name":"shravan",
    "email":"shravanpitla180@gmail.com",
    "CGPA":7.27,
    "college":"marri laxman reddy "
}
print(Details)
#update
Details.update({"email":"shrvan180@gmail.com","CGPA":8.10,"college":"mlritm"})
print(Details)
#soreted
print(sorted(Details))