geral = []
par = []
impar = []
for c in range(0,7):
	n = int(input('INFORME UM VALOR: '))
	if n % 2 == 0:
		par.append(n)
	if n % 2 != 0:
		impar.append(n)

impar.sort()
par.sort()		
geral.append(impar)
geral.append(par)
print(geral)