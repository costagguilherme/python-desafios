import time
print('=====CALCULADORA=====')
n1 = int(input('1° VALOR: '))
n2 = int(input('2° VALOR: '))
print('=-'*40)
op = 0
lista = []
while op != 5:
    op = int(input('''OPERAÇÕES POSSÍVEIS:
    [1] SOMAR
    [2] MUTIPLICAR
    [3] MAIOR VALOR
    [4] NOVOS NÚMEROS
    [5] SAIR DO PROGRAMA
    ESCOLHA UMA OPÇÃO: '''))
    print('=-' * 25)
    if op == 1:
        soma = n1 + n2
        print(f'{n1} + {n2} = {soma}')
        print('=-' * 25)
    if op == 2:
        mult = n1 * n2
        print(f'{n1} x {n2} = {mult}')
        print('=-' * 25)
    if op == 3:
        lista = lista + [n1,n2]
        maior = max(lista)
        print(f'O MAIOR VALOR É: {maior}.')
        print('=-' * 25)
    if op == 4:
        print('ESCOLHA OS NOVOS VALORES!')
        n1 = int(input('1° VALOR: '))
        n2 = int(input('2° VALOR: '))
        print('=-' * 25)
    if op == 5:
        print('SAINDO DA CALCULADORA...')
        print('=-' * 25)
        time.sleep(2.5)
        print('VOLTE SEMPRE!')
    if op > 5:
        print('OPERAÇÃO INVÁLIDA, TENTE NOVAMENTE!')
        print('=-' * 25)