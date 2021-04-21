list = []
cont= 0
while True:
    list.append(int(input('INFORME UM VALOR: ')))
    cont = cont + 1
    next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    while next != 'S' and next != 'N':
        next = str(input('QUER CONTINUAR? S ou N: ')).upper().strip()
    if next == 'N':
        print('PROGRAMA ENCERRADO')
        break
print(f'{cont} VALORES FORAM INFORMADOS.')
if 5 in list:
    print('5 ESTÁ NA LISTA')
else:
    print('5 NÃO ESTÁ NA LISTA')
list.sort(reverse=True)
print(f'ORDEM DESCRESCENTE = {list}')
