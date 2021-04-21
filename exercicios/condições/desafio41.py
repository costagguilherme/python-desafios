a = int(input('INFORME SEU ANO DE NASCIMENTO: '))
i = 2020 - a
if i <= 9:
    print('CATEGORIA MIRIM')
elif 10 <= i <= 14:
    print('CATEGORIA INFANTIL')
elif 15 <= i <=19:
    print('CATEGORIA JUNIOR')
elif i == 20:
    print('CATEGORIA SÊNIOR')
else:
    print('CATEGORIA MASTER')