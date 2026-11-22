

#Taklif15_L5 

users = [     (1, "ali", "active"),     (2, "sara", "inactive"),     (3, "reza", "active"),     (4, "mina", "inactive"),     (5, "nima", "active") ]

username = input('Enter Username:')

for info in users:
    id = info[0]
    name = info[1]
    status = info[2]
    
    if username == name:
        print('ID:', id, 'Status:',status)
        break
else:
    print('Username is Wrong')
        

"""

Enter Username:sara
ID: 2 Status: inactive

"""

"""

Enter Username:hasan
Username is Wrong

"""        