
n = int(input('Informe um valor: '))
print('-='*25)
continuar = str(input('Quer continuar? S ou N: ')).upper()[0].strip()
print('-='*25)
cont = 1
total = n
media = 0
lista = [n]
while 'S' in continuar:
    n1 = int(input('Informe outro valor: '))
    print('-=' * 25)
    total = total + n1
    cont = cont + 1
    media = total / cont
    continuar = str(input('Quer continuar? S ou N: ')).upper()[0].strip()
    print('-=' * 25)
    lista = lista + [n1]
    maior = max(lista)
    menor = min(lista)

if 'N' in continuar:
    print('PROGRAMA FINALIZADO.')
    print('-=' * 25)

elif continuar != 'N' and continuar != 'S':
    print('DIGITE UMA OPÇÃO VÁLIDA PARA CONTINUAR.')
    print('RESULTADOS ABAIXO:')
    print('-=' * 25)

print(f'{cont} NÚMEROS INFORMADOS.')
print(f'MÉDIA = {media}')
print(f'MAIOR VALOR = {maior}')
print(f'MENOR VALOR = {menor}')