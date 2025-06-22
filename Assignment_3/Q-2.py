def add(a, b):
    print(a + b)
def sub(a, b):
    print(a - b)
def pro(a, b):
    print(a * b)
def div(a, b):
    print(a / b)

x = int(input("Input first Value: "))
y = int(input("Input Second Value: "))
op = input("Enter Operation to perform *, -, /, + : ")
if op == "*":
    pro(x, y)
elif op == "-":
    sub(x, y)
elif op == "/":
    div(x, y)
elif op == "+":
    add(x, y)
else:
    print("Invalid Choice")
