n1 = int(input('INFORME UM VALOR: ')), int(input('INFORME UM VALOR: ')), int(input('INFORME UM VALOR: ')), int(input('INFORME UM VALOR: '))
print(f'Você digitou os valores: {n1}')
if 3 in n1:
    print(f'O valor 3 apareceu na {n1.index(3) + 1}° posição.')
if 9 in n1:
    print(f'O valor 9 apareceu {n1.count(9)} vezes.')
print('Os valores pares são: ', end='')
for n in n1:
    if n % 2 == 0:
        print(n, end=' > ')
print('FIM')