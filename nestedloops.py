# for loop:-writing 'for' inside a 'for' block

print("I J k")
for i in range(0,2):    
    for j in range(0,4):
        for k in range(0,3):
           print(i,j,k)

# #star patterns
# #increasing Triangle

# for i in range(0,6):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# #Decreasing Triangle
# for i in range(5,0,-1):
#     for j in range(i):
#         print("*",end=" ")
#     print()

# #square Triangle
# for i in range(0,6):
#     for j in range(0,6,):
#         print("*",end="")
#     print()

# #Rectangle triangle
# for i in range(0,4):
#     for j in range(0,8):
#         print("*",end=" ")
#     print()



# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(2*i-1):
#         print("*",end="")
#     print()

#printing pattern using numbers
# for i in range(1,6):
#     for j in range(1,i+1):
#         print(j,end=" ")
#     print()



# for i in range(1,6):
#     for j in range(1,i+1):
#         print(i,end=" ")
#     print()



# for i in range(1,6):
#     for j in range(5,5-i,-1):
#         print(j,end="")
#     print()

# num=1                              #1
# for i in range(1,5):               #23
#     for j in range(i):             #456
#         print(num,end="")          #78910
#         num+=1
#     print()

# for i in range(5):                  #54321
#     for j in range(5,0,-1):         #54321
#         print(j,end="")             #54321
#     print()                         #54321
#                                     #54321




# for i in range(5,0,-1):              #54321
#     for j in range(5,5-i,-1):        #5432
#         print(j,end="")              #543
#     print()                          #54
                                       #5


# for i in range(1,6):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()



#     1
#    123 
#   12345
#  1234567
# 123456789
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         print(j,end="")
#     print()

#     1
#    222
#   33333
#  4444444
# 555555555
# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(0,2*i-1):
#         print(i,end="")
#     print()




#CODE
# name="CODE"
# for i in range(1,len(name)+1):
#     for j in range(i):
#         print(name[j],end="")
#     print()

# name="CODE"
# for i in range(1,len(name)+1):
#     for j in range(i):
#         print(name[0],end="")
#     print()


# name="CODE"
# for i in range(1,len(name)+1):
#     for j in range(i):
#         print(name[i-1],end="")
#     print()

# name="CODE"
# for i in range(0,len(name)):
#     for j in range(i):
#         print(name[i],end="")
#     print()


# n=5
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,2*i):
#         if i==n:
#             print("*",end="")
#         elif j==1 or j==2*i-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()