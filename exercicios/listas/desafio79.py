list = []
while True:
    list.append(int(input('INFORME UM VALOR: ')))
    next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    while next != 'S' and next != 'N':
        next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    if next == 'N':
        print('PROGRAMA ENCERRADO')
        break
    a = (list)
    b = sorted((set(list)))
print(f'LISTA = {a}')
print(f'LISTA ORDENADA SEM REPETICÇÕES = {b}')