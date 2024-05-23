valor_da_tv = float(input())
quant_parcelas = int(input())

if quant_parcelas == 1:
    juros = 0
elif quant_parcelas == 2:
    juros = 5
elif quant_parcelas == 3:
    juros = 10
elif quant_parcelas == 4:
    juros = 15
elif quant_parcelas == 5:
    juros = 20
elif quant_parcelas == 6:
    juros = 25
elif quant_parcelas == 7:
    juros = 30
elif quant_parcelas == 8:
    juros = 35
elif quant_parcelas == 9:
    juros = 40
elif quant_parcelas == 10:
    juros = 45
else:
    juros = None

if juros is not None:
    
    # calculando o valor total com juros
    valor_total = valor_da_tv * (1 + juros / 100)
    
    # calculando o valor da parcela
    valor_parcela = valor_total / quant_parcelas

    print(f'{valor_parcela:.2f}')
    print(f'{valor_total:.2f}')
