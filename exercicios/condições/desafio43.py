p = float(input('Informe o seu peso: '))
h = float(input('Informe sua altura: '))
i = p / (h ** 2)
if i < 18.5:
    print('ABAIXO DO PESO')
elif 18.5 <= i < 25:
    print('PESO IDEAL')
elif 25 <= i < 30:
    print('ACIMA DO PESO')
elif 30 <= i < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')