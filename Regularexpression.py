# '''
# Regular Expression :- It is a pattern used to search, match, extract or validate text

# '''
# #re.search() - Search looks for a pattern anywhere inside string
# import re
# text = "I'm learning Python"
# result = re.search("Python",text)
# print(result)

# # we need to use search when we want to know as "does this pattern occur somewhere in text."

# # re.math -->IT checks the pattern only at the beginning

# import re
# text = "From the day one, I'm focusing on and it is easy"
# result = re.match("Python",text)
# print(result)

# #re.fullmatch()-->It requies entire string to match the pattern

# import re
# text = "Python"
# result = re.fullmatch("Python",text)
# print(result)

# # re.findall()-->It finds all occurences of a pattern and return then as a list
# import re
# text = "I have 10 apples and 20 oranges"
# result = re.findall(r"\d+",text)
# print(result)

# #\d - digits (digits from 0 to 9)
# # \d+ -combination of one or more digits

# import re
# text = "I have 10 apples and 20 oranges"
# result2 = re.findall(r"\d",text)
# print(result2)

# # \w - word character
# # -letters
# # -Digits
# # -Underscore(_)
# import re
# text = "Pyhton_12345"
# result = re.findall(r"\w",text)#we can also write (\w+):-o\p:-['Pyhton_12345']
# print(result)

# # ^ - Start of String
# # The pattern must start at beginning

# import re
# pattern = r"^Python"
# print(re.search(pattern,"Python is easy")) 

# # $ --> Pattern must end at the of string
# import re
# pattern = r"Python$"
# print(re.search(pattern,"is easy Python")) 


# # r"^\d{4}$"
# #Quantifiers - It tells regular Expression how many times can occur *, +, ?, {}

# #* - Zero or More
# # r"ab*"- a, ab, abb, abbb, abbbb, abbbbb.....
# # becausse b can occur zero or more times

# # +-->One or more
# #R"ab+" --> ab, abb, abbb, abbbb, abbbb, abbbbb
# # a is not valid here, because atleast 1 b needs to be there

# # ? -->Xero or More
# #r"colou?r -->color, colour

# #{} --> Exact Number
# # r"^\d{4}$" --> means exactly 4 digits
# # 1234(correct), 123(wrong), 12345(wrong).
# # #r"^\d(4,6)$ -->means 4 to 6 digits are valid

# #Digits validation

# import re
# value = input()
# pattern = r"^\d+$"

# if re.fullmatch(pattern, value):
#     print("Only Digits")
# else:
#     print("Invalid")


# #Phone Number Validation
# import re
# phone = input("Enter number: ")
# pattern = "^[6-9]\d{9}$"
# if re.fullmatch(pattern,phone):
#     print("Valid")
# else:
#     print("Invalid")



# #Email validation
# #username@domain.com
# r"^[\w.-]+@[\w.-]+\.\w+$"
# # [\w.-]+ - username
# # [\w.-]+ - domain
# import re
# Email = input("Enter email address: ")
# pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
# if re.fullmatch(pattern,Email):
#     print("Valid")
# else:
#     print("Invalid")

#Name and Password validation
import re
name = input("Enter name: ")
password = input("Enter password: ")
if re.fullmatch(r"[A-Za-z]+", name):
    print("Valid")
else:
    print("Invalid")
pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
if re.fullmatch(pattern,password):
    print("Valid")
else:
    print("Invalid")

#  r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d).{8,}$"
# (r) --> raw string
# (^) --> Start of string
# (?)(=)(.) --> It checks whether the condition exists,but don't remove characters
# check --> is the condition satisfied
# (*) --> zero or More 
# ?=.*[A-Z] --> It checks the Password that atleast contain one uppercase letter
