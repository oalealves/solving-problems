x = int(input())
x2 = int(input())
operador = input()

if operador == "+":
    resultado = x + x2
elif operador == "-":
    resultado = x - x2
elif operador == "*":
    resultado = x * x2
elif operador == "/":
    resultado = x // x2

print(resultado)
