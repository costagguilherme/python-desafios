from time import sleep
def contador(i, f, p):
    print(f'O CONTADOR DE {i} até {f} pulando de {p} em {p} é: ')
    cont = 1
    cont1 = i
    if i < p:
        while cont <= f:
            print(f'{cont}', end=' - ')
            sleep(0.4)
            cont = cont + p
        print('FIM')
    if i > f:
        while cont1 >= f:
            print(f'{cont1}', end=' - ')
            sleep(0.4)
            cont1 = cont1 - p
        print('FIM')
contador(1,10,2)
contador(10,1,2)
print('AGORA FAÇA SUA CONTAGEM PERSONALIZADA: ')
a = int(input('INFORME O INICIO: '))
b = int(input('INFORME O FIM: '))
c = int(input('INFORME O PASSO: '))
print(f'CONTAGEM PERSONALIZADA DE {a} até {b} pulando de {c} em {c}.')
contador(a,b,c)