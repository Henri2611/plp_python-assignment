user_input1= input("Enter first number: ");
user_input2= input("Enter second number: ");
sign = input("Enter the sign(+,-,* ,/): ")

value1 = int(user_input1)
value2 = int(user_input2)

if sign == '+':
    print(f"{value1 } + {value2} = {value1 + value2} ")
elif sign == '-':
    print(f"{value1 } - {value2}  = {value1 - value2} ")
elif sign == '*':
    print(f" {value1 } * {value2} = {value1 * value2} ")
elif sign == '/':
    if value2 != 0:
         print(f" {value1 } / {value2} = {value1 / value2} ")
        
    else:
        print("cannot divide by zero")
       
