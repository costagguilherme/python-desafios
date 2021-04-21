num = []
for c in range(0,5):
    num.append(int(input('INFORME UM VALOR: ')))
    maior = max(num)
    menor = min(num)
print(f'MAIOR = {maior}')
print(f'MENOR = {menor}')
a = num.index(maior)
b = num.index(menor)
print(f'POSIÇÃO DO MAIOR = {a}', end=' > ')

cont = 1
while cont < num.count(maior):
    print(f'{num.index(maior, a + cont)}', end=' > ')
    cont = cont + 1
print('...')

print(f'POSIÇÃO DO MENOR = {b}', end=' > ')
cont1 = 1
while cont1 < num.count(menor):
    print(f'{num.index(menor, b + cont1)}', end=' > ')
    cont1= cont1 + 1
print('...')