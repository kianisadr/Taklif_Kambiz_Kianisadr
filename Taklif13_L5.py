

#Taklif13_L5


high_score = []

students = [     ("Ali", 18),     ("Sara", 12),     ("Reza", 9),     ("Mina", 20),     ("Nima", 14) ]

for info in students:
    name = info[0]
    score = info[1]
    if score >= 15:
        high_score.append(name)
print(high_score)                 #['Ali', 'Mina']
    

