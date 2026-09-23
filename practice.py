employee = {
    "name": " shravan",
    "projects":5,
    "rating":0
    }
print(employee)
# employee=input("enter rating and project")
if employee["rating"]>=4 and employee["projects"]>=5:
    print("excellent")
elif employee["rating"]>=3 and employee["projects"]>=3:
    print("Good")
elif employee["rating"]>=2:
    print("Needs improvement")
else:
    print("poor")
