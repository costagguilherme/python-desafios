total = 0
contp = 0
lista = []
barato = ''
while True:
    nome = str(input('INFORME O NOME DO PRODUTO: ')).upper().strip()
    p = int(input('INFORME O PREÇO DO PRODUTO: R$'))
    if p > 1000:
        contp = contp + 1
    total = total + p
    lista = lista + [p]
    pmenor = min(lista)
    if p == pmenor:
        barato = nome


    next = str(input('QUER CONTINUAR? [S ou N]: ')).upper().strip()
    if next == 'N':
        print('PROGRAMA ENCERRADO.')
        break
    while next != 'S' and next != 'N':
        next = str(input('QUER CONTINUAR? [S ou N]: '))

print(f'TOTAL = {total}')
print(f'{contp} PRODUTOS CUSTAM MAIS DE R$1000')
print(f'O PRODUTO MAIS BARATO É O {barato}.')