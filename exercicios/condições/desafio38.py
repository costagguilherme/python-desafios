n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print(f'{n1} é o maior valor')
elif n2 > n1:
    print(f'{n2} é o maior valor')
else:
    print('Os dois são iguais')