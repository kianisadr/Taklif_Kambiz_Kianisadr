

#Taklif06_L4

number1 = int(input('Enter the first number:'))

number2 = int(input('Enter the second number:'))

operation = input("Enter your Operation:")

if operation == '+':
    result = number1 + number2
    print('Result =', result)
elif operation == '-':
    result = number1 - number2
    print('Result =', result)
elif operation == '*':
    result = number1 * number2
    print('Result =', result)
elif operation == '//':
    result = number1 // number2
    print('Result =', result)
else:
    print('Your Operation is Wrong')
    
    
"""

Enter the first number:12
Enter the second number:4
Enter your Operation://
Result = 3


Enter the first number:24
Enter the second number:6
Enter your Operation:d
Your Operation is Wrong

"""    
    
    

