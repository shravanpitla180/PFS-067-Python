# # #Password Generator using random
# import random

# character = "@#$%^&*-+abcdefghijklmnopqrstuvwxyz"
# password = ""
# for i in range(10):
#     password +=random.choice(character)
# print("password:",password)


# #Password generator using string
# import random
# import string

# characters = string.ascii_letters + string.digits + string.punctuation
# password=" "
# for i in range(10):
#     password +=random.choice(characters)
# print("password:",password)



# #ATM Example
# # check pin
# correct_pin =1234

# pin = int(input("Enter Pin:"))
# if pin == correct_pin:
#     print("Access granted")
# else:
#     print("Invalid Pin")
    
# #Add Balance
# Balance = 11000
# deposit = 4000
# pin = int(input("Enter Pin :"))
# if pin == 1234:
#     print("Access Granted")
#     Balance += deposit   
#     print(Balance)
# else:
#     print("Invallid Pin") 
    
# #Withdraw money
# balance = 10000
# pin = int(input("Enter Pin :"))
# if pin == 1234:
#     amount =int(input("Enter withdraw amount: "))
#     if amount<=balance:
#         balance -=amount
#         print("Withdraw successful")
#         print("Remaining Balance :",balance)
#     else:
#         print("Insufficient Balance")
# else:
#     print("Invalid Pin")
    
    
    
#Complete ATM Exmple

Balance = 50000
pin = int(input("Enter pin: "))
if pin == 1234:
    print("\n1.check Balance")
    print("2.Withdraw")
    print("3.Deposite")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Balance: ",Balance)
    elif choice ==2:
        amount=int(input("Enter withdraw amount: "))
        if amount <=Balance:
            Balance -=amount
            print("Withdraw Successful")
            print("remaining Balance: ",Balance) 
        else:
            print("Insufficent Balance")
    elif choice ==3:
           amount=int(input("Enter amount: "))
           Balance +=amount
           print("Deposite success")
           print("Updated balance:",Balance)
    else:
        print("Invalid choice")
else:
    print("Pin Incorrect")