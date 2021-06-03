def add(x,y):
    return x + y
def subtract(x,y):
    return x - y
def multiply(x,y):
    return x * y
def divide(x,y):
    return x / y
 
print("Please select choice\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")
choice = int(input("Select operations form 1, 2, 3, 4 :"))
 
number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))
 
if choice == 1:
    print(number_1, "+", number_2, "=", add(number_1, number_2))
 
elif choice == 2:
    print(number_1, "-", number_2, "=", subtract(number_1, number_2))
 
elif choice == 3:
    print(number_1, "*", number_2, "=", multiply(number_1, number_2))
 
elif choice == 4:
    print(number_1, "/", number_2, "=",divide(number_1, number_2))
else:
    print("Invalid input")


