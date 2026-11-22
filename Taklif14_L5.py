

#Taklif14_L5

products = [     ("Laptop", 50000, 2),     ("Mouse", 800, 3),     ("Keyboard", 1500, 2),     ("Monitor", 12000, 1) ]

total_price = 0

for info in products:
    product = info[0]
    price = info[1]
    number = info[2]
    
    total_amount = price * number
    print('Total Amount:',total_amount)
    
    total_price = total_price + total_amount
print('Total Price of Producs:', total_price)


"""

Total Amount: 100000
Total Amount: 2400
Total Amount: 3000
Total Amount: 12000
Total Price of Producs: 117400

"""    


