

#Taklif16_L5

 
students = [("Ali", 22, 18),("Sara", 20, 15), ("Reza", 23, 9),("Mina", 21, 20),("Nima", 19, 12), ("Amir", 24, 7) ]

total_score = 0
highest_score = 0
highest_score_student = ""
low_scores = []

for student in students:
    name = student[0]
    age = student[1]
    score = student[2]
    print('Name:', name, '-', 'Age:', age, '-', 'Score:', score)
    
    total_score = total_score + score
    
    if score < 10:
        low_scores.append(name)
print('Low scores students:', low_scores)
            
    
if score > highest_score:
    highest_score = score
    highest_score_student = name
        
    average_score = total_score / len(students)    
print('Average Scores:', average_score)
    
for student in students:
    name = student[0]
    score = student[1]
    
if score > average_score:
        
    print('Higher average Score Students:', name)    
    
    
"""

Name: Ali - Age: 22 - Score: 18
Name: Sara - Age: 20 - Score: 15
Name: Reza - Age: 23 - Score: 9
Name: Mina - Age: 21 - Score: 20
Name: Nima - Age: 19 - Score: 12
Name: Amir - Age: 24 - Score: 7
Low scores students: ['Reza', 'Amir']
Average Scores: 13.5
Higher average Score Students: Amir

"""   
          
   
    
   
    
    
    
        
    

