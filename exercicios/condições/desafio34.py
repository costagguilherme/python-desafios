s = int(input('Qual o seu salário?'))
a1 = s + ((10 * s) / 100)
a2 = s + ((15 * s) / 100)
if s > 1250:
    print(f' Seu novo salário será {a1}')
if s <= 1250:
    print(f'Seu novo salário será {a2}')