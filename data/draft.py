hora = int(input())
minuto = int(input())
dia = int(input())
mes = int(input())
ano = int(input())
ultimos_digitos = ano % 100

print(f'{hora:02d}:{minuto:02d} {dia:02d}/{mes:02d}/{ultimos_digitos:02d}')