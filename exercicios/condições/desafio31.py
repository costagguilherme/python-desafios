d = int(input('Qual é a distância da viagem em km? '))
p1 = d * 0.5
p2 = d * 0.45
if d <= 200:
    print(f'O custo da viagem foi {p1}R$')
else:
    print(f'O custo da viagem foi {p2}R$')