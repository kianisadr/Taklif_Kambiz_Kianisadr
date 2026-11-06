
#Tklif3_L2


product = input('what is your product name?:')

price = float(input('How much is your price?:'))

discount = int(input('How much is the discount?:'))

discounted_price = price * discount / 100

final_price = price - discounted_price

new_product = product.upper().replace(" ","")

print('Final Price of', new_product,'is', final_price)

"""

what is your product name?:IPhone 16PRO
How much is your price?:15000000
How much is the discount?:20
Final Price of IPHONE16PRO is 12000000.0

"""


