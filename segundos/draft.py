total_de_segundos = int(input())

horas = total_de_segundos // 3600

resto_de_tempo = total_de_segundos % 3600

minutos = resto_de_tempo // 60

segundos = resto_de_tempo % 60

print(f'{horas}:{minutos}:{segundos}')
