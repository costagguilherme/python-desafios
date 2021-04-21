a1 = int(input('Informe o 1° termo: '))
r = int(input('Informe a razão: '))
n = 1
while n <=10:
	an = a1 + (n - 1) * r
	print(f'a{n} = {an}')
	n = n + 1