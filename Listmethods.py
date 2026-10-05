#1.List[]
list=[1,2,3,4,5,]
print(list)
#Append()
list.append(6)
print(list)
#Extend()
a=[1,2,3,4]
b=[5,6,7,8]
print(a+b)
#Insert()
list=[10,20,30]
list.insert(2,55)
print(list)

#2.Access elements using indexing
name="shravan"
print(name)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

#3.Access elements using negative indexing
name="shravan"
print(name)
print(name[-1])
print(name[-2])
print(name[-3])
print(name[-4])
print(name[-5])
print(name[-6])
print(name[-7])

#4.slicing
list=[1,2,3,4,6]
print(list[1:4])

#5.Modify an existing elements
list=[10,20,30,40]
list[2]=99
print(list)

#Remove()
list=[11,22,33,44,55]
list.remove(11)
print(list)

#pop()
list=[10,12,18,20,25,88] 
list.pop()
print(list)

#clear()
list=[10,20,30,40,55]
list.clear()
print(list)

#find the number of elements using len()
#7.len()
list=[10,20,30,40,50]
n=len(list)
print(n)

#8.search for an element using (in)
list=[11,54,63,78,21,12]
print(12 in list)

#9.Find the position of an element using index()
list=[10,20,30,50,40,60]
n=list.index(50)
print(n)

#10.count occurence using count()
list=[10,10,20,22,10,22,50,54,45,55,20,44,44,10,48,10,10]
n=list.count(44)
print(n)

#11.Sort the list using Sort()
list=[11,10,9,8,7,5,4,6,2,1,3]
list.sort()
print(list)

#12.Reverse the list using reverse()
num=[50,40,30,20,10]
n=num[::-1]
print(n)

#13.Create a copy using copy()
list=[10,20,30,40,44]
n=list.copy()
print(n*2)