lista = []
for c in range(1,8):
   p = float(input(f'Informe o peso da {c}° pessoa: '))
   lista = lista + [p]
maior = max(lista)
menor = min(lista)
print(f'O maior pesso foi {maior}')
print(f'O menor peso foi {menor}')
