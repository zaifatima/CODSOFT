def add(n1, n2):
    return n1 + n2
 
def subtract(n1, n2):
    return n1 - n2
 
def multiply(n1, n2):
    return n1 * n2
 
def divide(n1, n2):
    return n1 / n2
 
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
 

select = int(input("Select operations form 1, 2, 3, 4 :"))
 
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
 
if select == 1:
    print(number1, "+", number2, "=",
                    add(number1, number2))
 
elif select == 2:
    print(number1, "-", number2, "=",
                    subtract(number1, number2))
 
elif select == 3:
    print(number1, "*", number2, "=",
                    multiply(number1, number2))
elif select == 4:
    print(number1, "/", number2, "=",
                    divide(number1, number2))
else:
    print("Invalid input")
