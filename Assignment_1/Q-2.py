a = int(input("Enter any value: "))
b = int(input("Enter any value: "))

op = input("Enter operator +, -, *, /, % : ")
if op == "+":
    print(a+b)
elif op == "-":
    print(a - b)
elif op == "*":
    print(a * b)
elif op == "/":
    print(a / b)
elif op == "%":
    print(a % b)
else:
    print("Invalid operator")