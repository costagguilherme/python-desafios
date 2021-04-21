n = 0
soma = 0
cont = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont = cont + 1
    soma = soma + n
print(f'{cont} números foram digitados.')
print(f'Soma = {soma}')