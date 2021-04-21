soma = 0
c3 = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
linha2 = []
for l in range (0,3):
	for c in range(0,3):
		matriz[l][c]= int(input(f'Digite o valor da posição [{l} {c}]: '))
		if matriz[l][c] % 2 == 0:
			soma = soma + matriz[l][c]
		if c == 2:
			c3 = c3 + matriz[l][c]
		if l == 1:
			linha2.append(matriz[l][c])
			maior = max(linha2)
		
for l in range(0,3):
	for c in range(0,3):
		print(f'[{matriz[l][c]:^5}]', end=' ')
	print('')

print(f'MAIOR VALOR DA LINHA 2 = {maior}')
print(f'SOMA DOS PARES = {soma}')
print(f'SOMA DA COLUNA 3 = {c3}')