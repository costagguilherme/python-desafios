while cont <= 5:
    a = (random.randint(0,10))
    cont = cont + 1
    print(a, end=' -> ')
    lista = lista + [a]
    maior = max(lista)
    menor = min(lista)
print('FIM')
print(f'MAIOR VALOR = {maior}')
print(f'MENOR VALOR = {menor}')