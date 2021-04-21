num = int(input('Escolha um número: '))
cont = 0
for c in range(1, num +1):
    if num % c == 0:
        cont = cont + 1
if cont == 2:
    print('Este número é PRIMO!!')
else:
    print(f'Este número é divisível por {cont} números, então ele NÃO É PRIMO!!')