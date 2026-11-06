

#Taklif2_L3

scores = [15, 18, 12, 20,16]

scores.append(19)

print(scores)     #[15, 18, 12, 20, 16, 19]

#------------------------

scores.remove(12)

print(scores)     #[15, 18, 20, 16, 19]

#------------------------

scores[1] = 17

print(scores)     #[15, 17, 20, 16, 19]

#------------------------

scores.insert(2, 14)

print(scores)      #[15, 17, 14, 20, 16, 19]

#------------------------

scores.sort()

print(scores)     #[14, 15, 16, 17, 19, 20]

#------------------------

scores.reverse()

print(scores)     #[20, 19, 17, 16, 15, 14]

#------------------------











