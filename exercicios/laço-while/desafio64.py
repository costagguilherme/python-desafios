n = int(input('Informe um valor [999 pra interromper]: '))
cont = 0
soma = 0
while n != 999:
    cont = cont + 1
    soma = soma + n
    n = int(input('Informe um valor [999 pra interromper]: '))
print('=-'*25)
if n == 999:
    print('FIM DO PROGRAMA')
print('=-'*25)
print(f'{cont} valores foram digitados')
print('=-'*25)
print(f'A soma destes valores é {soma}')