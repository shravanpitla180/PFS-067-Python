#set-Unoredered set of unique elements
#   {}
#set
name={10,20,30,40,50}
print(name)
#another way to create set
num=set()
print(type(num))
#add()
set={10,20,30}
set.add(40)
print(set)

#set Operations
#union,intersection,difference,symmetric diff

#union-combine all the sets from both sets,with duplicates
A={10,20,30}
B={10,40,50}
print(A | B)
#Using another method
print(A.union(B))

#Intersection-common elements
print(A&B)
print(A.intersection(B))

#Differnce-Elements that exist in the first set but not in the second
print(A-B)
print(B-A)

#symmetric diff-elmemets that are in either set but in both
print(A^B)

#set methods
#update()
set={10,20,30}
set.update([50,60,70])
print(set)
#remove()
set.remove(60)
print(set)
#discard()-safest operation(to not come error we use discard)
set.discard(10)
print(set)
#pop()
set.pop()
print(set)
#clear()
set.clear()
print(set)
#len()
t={10,20,30}
m=len(t)
print(m)
#max()
lst={10,20,30,40}
print(max(lst))
#min()
lst={10,20,30,40}
print(min(lst))
#sum()
lst={10,20,30,40}
print(sum(lst))
#add()
lst={10,20,30,40}
lst.add(60)
print(lst)
