def add(a, b): return a + b
def sub(a, b): return a - b
def mul(a, b): return a * b
def div(a, b): return a / b if b != 0 else "Cannot divide by 0"

x = float(input("First number: "))
y = float(input("Second number: "))
op = input("Operator (+ - * /): ")

if op == "+": print(add(x, y))
elif op == "-": print(sub(x, y))
elif op == "*": print(mul(x, y))
elif op == "/": print(div(x, y))
else: print("Invalid operator")