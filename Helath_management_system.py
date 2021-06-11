# Project 3
# Gym Management System
# Clint can log or 

def getdate():
    import datetime 
    return datetime.datetime.now()
print("This is a Helath management system\nHere you can simply log your exercise and dite details\nWhich you can retrive the loged data")
def log():
    """It is used to log data in a text file"""
    name = input("Enter username: ")
    a = int(input(f"{name} What do you want to choose\n   1 for exerxcise and\n   2 for dite\n"))
    if a == 1:
        x= input("Enter The Exercise\n")
        with open(f"{name}ex.txt", "a") as f:
            f.write(str([str(getdate())]) + ": " + x + "\n")
            print(f"Added sucessfully in :{name}ex.txt")
    elif a==2:
        x= input("Enter The Exercise\n")
        with open(f"{name}dite.txt", "a") as f:
            f.write(str([str(getdate())]) + ": " + x + "\n")
            print("Added sucessfully in :{name}dite.txt")

def retrive():
    """It is used to retrive loged data from a text file"""
    name = input("Enter username: ")
    a = int(input(f"{name} What do you want to choose\n   1 for exerxcise and\n   2 for dite\n"))
    if a == 1:
        with open(f"{name}ex.txt") as f:
            a = f.read()
            print(a)    
    elif a ==2:
        with open(f"{name}dite.txt") as f:
            a = f.read()
            print(a)                 
    else:
        print("Please Enter a valid input")
a = int(input("Select the option:\n 1 for log\n 2 for retrieve\n"))
if a == 1:
    log()
elif a == 2:
    retrive()
else:
    print("Please Enter a valid input")
