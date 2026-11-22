

#Taklif05_L5

numbers = [12, 7, 25, 18, 3, 40, 11, 8]
count = 0
even_number_list = []

for number in numbers:
    if number % 2 == 0:
        even_number_list.append(number)
        count = count + 1
        
print('Even Number Count:',even_number_list)        
print('Even Number Count =', count)


"""

Even Number Count: [12, 18, 40, 8]
Even Number Count = 4

"""
        