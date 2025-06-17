temperatura = float(input('Digite a temperatura atual em graus Celsius:'))
if temperatura < 0:
    print('Congelante!')
    if temperatura < -10:
        print('Risco de hipotermia!')
elif temperatura >= 30:
    print('Dia quente!')
    if temperatura > 35:
        print('Risco de insolação!')