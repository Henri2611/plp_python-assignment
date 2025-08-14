# def calculate_discount(price, discount_percent):
     
#     if discount_percent >= 20:
#       discount = (discount_percent / 100) * price
#       final_price = price - discount
#       return f"The price will be {final_price} ksh"
#     else:
#         return f"The price will be {price} ksh"
# print(calculate_discount(5000, 20))
        

def calculate_discount(price, discount_percent):
     
    if discount_percent >= 20:
        discount = (discount_percent / 100) * price
        final_price = price - discount
        print(f"The price will be {final_price} ksh")
    else:
        print(f"The price will be {price} ksh")
#prompt user
price = int(input("Enter the price: "))
discount_percent = int(input("Enter the discount percentage: "))

#display result
calculate_discount(price, discount_percent)