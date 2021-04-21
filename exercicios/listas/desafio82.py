list = []
par = []
impar = []
while True:
    list.append(int(input('INFORME UM VALOR: ')))
    next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    while next != 'S' and next != 'N':
        next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    if next == 'N':
        print('PROGRAMA ENCERRADO')
        break
print(f'LISTA = {list}')
for pos in range(0, len(list)):
    if list[pos] % 2 == 0:
        par.append(list[pos])
    elif list[pos] % 2 != 0:
        impar.append(list[pos])
print(f'PAR = {par}')
print(f'IMPAR = {impar}')