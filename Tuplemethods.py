#1.Tuple
tuple=(21,7.27,"shravan",True,[1,2,3],{"key":"value"})
print(tuple)
print(type(tuple))

#2.using indexing
tuple=(10,20,30,40,44)
print(tuple[2])
#-----
n=tuple.index(20)
print(n)

#using negative indexing
tuple=("shravan")
print(tuple[-1])
print(tuple[-2])
print(tuple[-3])
print(tuple[-4])
print(tuple[-5])
print(tuple[-6])
print(tuple[-7])

#slicing
tuple=(10,20,30,50,40)
n=tuple[1:4]
print(n)

#len()
tuple=(11,22,33,4,55,66,4,7,2,11,20)
n=len(tuple)
print(n)

#index()
tuple=(10,20,30,40,50)
n=tuple.index(30)
print(n)

#count()
tuple=(10,10,20,10,50,40,10,70,40,50,44,44,30)
n=tuple.count(10)
print(n)

#converting tuple() into list[]& mosify
tuple=(10,20,30,40)
new=list(tuple)
print(new)
new.append(50)
print(new)

lst=[10,20,30]
n=(*lst,)
print(n)


#concatination
a=(10,20,30)
b=(40,50,60)
n=a + b
print(n)

#slicing
a=(12,10,20,30,40,50,60,70,)
n=(a[1:6])
print(n)

#len()
lst=(10,20,30)
n=len(lst)
print(n)

#index
lst=(10,20,30,40,50)
n=lst.index(50)
print(n)

#count()

lst=(10,20,30,40,50,40,60,80,40,50,220,40,22,40)
n=list(lst)
print(n)
n.append(11)
print(n)

n2=tuple(n)
print(n2)