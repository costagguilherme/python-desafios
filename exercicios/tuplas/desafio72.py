a = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'cartoze', 'quinze')
n = int(input('DIGITE UM NÚMERO DE 0 A 15: '))
if n > 15 or n < 0:
    while True:
        n = int(input('DIGITE UM NÚMERO DE 0 A 15: '))
        if 0 <= n <= 15:
            break
print(f'Você digitou o numéro {a[n]}')