

#Taklif03_L4

amount = int(input("Enter the Amount (Toman):"))

if amount >= 1000000:
    print("Shipping Cost is Free")
    
elif amount >= 500000:
    print("Shipping Cost = 30000T")
    
else:
    print("Shipping Cost = 60000T")


"""

Enter the Amount (Toman):1000000
Shipping Cost is Free

    
Enter the Amount (Toman):550000
Shipping Cost = 30000T

Enter the Amount (Toman):320000
Shipping Cost = 60000T

"""


