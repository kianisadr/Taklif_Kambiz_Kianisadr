

#Taklif05_L4

name = ["Ali", "Kambiz", "Soheila", "Maryam", "Sara"]

passkey = 'python123'

user_name = input("Enter your username:")

password = input("Enter your password:")


if user_name not in name:
    print('User not Found')
    
elif password == passkey:
    print('Welcome')
    
else:
    print('Password is Wrong')
    
    
"""

Enter your username:Ali
Enter your password:python123
Welcome

"""

"""

Enter your username:Ali
Enter your password:asde
Password is Wrong

"""







