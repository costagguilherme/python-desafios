from random import randint
def sorteia(lista):
    print('OS NÚMEROS SORTEADOS FORAM: ', end=' ')
    for n in range(0,5):
        lista.append(randint(1,10))
        print(f'{lista[n]}', end=' - ')
    print('FIM')

def somapar(lista):
    soma = 0
    for n in numeros:
        if n % 2 == 0:
            soma = soma + n
    print(f'A SOMA DOS NÚMEROS PARES DA LISTA {numeros} É IGUAL À {soma}')

numeros = []
sorteia(numeros)
somapar(numeros)