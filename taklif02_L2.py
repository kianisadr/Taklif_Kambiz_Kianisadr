#T2_L2

goods_name = input('what is the goods_name?:')

price = float(input('How much is it?:'))

discount = price * 25 / 100

final_price = price - discount

new_name = goods_name.title()

print('Goods Name is', new_name,'and Final Price is', final_price)

"""

what is the goods_name?:table
How much is it?:10000
Goods Name is Table and Final Price is 7500.0

"""




