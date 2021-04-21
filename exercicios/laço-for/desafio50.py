s = 0
for c in range(1, 7):
    c = int(input('Digite um número inteiro: '))
    if c % 2 == 0:
        s = s + c
print(f'A soma dos números pares é {s}')