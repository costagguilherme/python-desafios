a = int(input('Digite um ano qualquer: '))
r = a % 4
if r <= 0:
    print(f'O ano {a} é bissexto')
else:
    print(f'O ano {a} não é bissexto')