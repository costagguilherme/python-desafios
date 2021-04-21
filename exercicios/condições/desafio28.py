import random
print('O computador irá pensar um número de 0 a 5, se você adivinhar qual este número, irá vencer!!')
num = int(input('Qual o número você acha que o computador pensou? '))
a = random.randint(0,5)
if num == a:
    print('Você venceu, parabéns!!!')
else:
    print('Você perdeu!!!')
print(f'O computador pensou no número {a}')