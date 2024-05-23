import math

#três lados do triângulo
a = float(input())
b = float(input())
c = float(input())

#semi-perimetro
perimetro = (a + b + c) / 2
#formula de Heron
area = perimetro * (perimetro - a) * (perimetro - b) * (perimetro - c)
#descobrindo a raiz quadrada
resultado = math.sqrt(area)

print(f'{resultado:.2f}')
