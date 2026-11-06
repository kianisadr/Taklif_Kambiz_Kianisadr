

#Taklif04_L4

password = input("Enter your Password:")

if len(password) < 8:
    print("Password is Short")
    
if password.isdigit():
    print("Password is Only Number")
    
if " " in password:
    print("Password has Space")
    
""" 

Enter your Password:12 345
Password is Short
Password has Space

"""

password = input("Enter your Password:")

if len(password) < 8:
    print("Password is Short")
    
    if password.isdigit():
        print("Password is Only Number")
    
        if " " in password:
            print("Password has Space")
        
    
"""

Enter your Password:123 456
Password is Short

در روش ایف های تو در تو اول شرط اول را بررسی می کند و اگر True باشد دیگر ادامه نمی دهد چون ایف های دیگر داخل خلقه ایف اول هستند 
"""    
    
    
password = input("Enter your Password:")

if len(password) < 8:
    print("Password is Short")
    
elif password.isdigit():
    print("Password is Only Number")
    
elif " " in password:
    print("Password has Space")

else:
    print(password)
    
    
"""

Enter your Password:123 456
Password is Short

در اینجا هم شرط اول ابتدا بررسی می شود و در صورتیکه درست باشد همانجا قطع می شود. 

"""    
    
