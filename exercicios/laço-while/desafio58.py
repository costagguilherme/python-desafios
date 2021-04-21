import random
print('O computador irá pensar um número de 0 a 10, se você adivinhar qual este número, irá vencer!!')
num = int(input('Qual o número você acha que o computador pensou? '))
a = random.randint(0,11)
cont = 0
while num != a:
    cont = cont + 1
    if num < a:
        num = int(input('Mais ...Digite outro número: '))
    if num > a:
        num = int(input('Menos ...Digite outro número: '))
print('Você venceu!')
print(f'Acertou com {cont} tentativas!')