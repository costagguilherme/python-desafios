s = 0
a1 = float(input('Informe o primeiro termo da P.A: '))
r = float(input('Informe a razão da P.A: '))
for n in range(1,11):
    an = a1 + (n - 1) * r
    print(f'a{n} = {an:.0f}')
