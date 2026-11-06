

#Taklif4_L3

student = ("Ali", 21, "Tehran")

new_student = list(student)


name = new_student[0]

print('Name is', name)

new_student[1] = 22

new_student[2] = "Shiraz"

result = tuple(new_student)

print(result)

"""

Name is Ali
('Ali', 22, 'Shiraz')

"""