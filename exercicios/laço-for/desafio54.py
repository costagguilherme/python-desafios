cont = 0
cont2 = 0
for c in range(1, 8):
    d = int(input(f'Informe a data de nascimento da {c}° pessoa: '))
    i = 2020 - d
    if i >= 18:
        cont = cont + 1
    else:
        cont2 = cont2 + 1
print(f'{cont} pessoas JÁ atingiram a maioridade.')
print(f'{cont2} pessoas ainda NÃO atingiram a maioridade')