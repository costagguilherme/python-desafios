f = str(input('Escreva uma frase: '))
a = f.replace(' ', '').upper()
b = a[::-1]
if a == b:
	print('A frase é um palíndromo')
else:
	print('A frase não é um palindromo')
