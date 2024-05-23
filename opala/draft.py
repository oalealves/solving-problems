velocidade = float(input())
tempo_min = float(input())
consumo = float(input())


tempo = tempo_min / 60

distancia = velocidade * tempo

desempenho = distancia / consumo




print(f'{desempenho:.2f}')

