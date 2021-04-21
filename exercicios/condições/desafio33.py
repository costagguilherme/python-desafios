a = int(input('Digite um número qualquer: '))
b = int(input('Digite um segundo número qualquer: '))
c = int(input('Digite um terceiro número qualquer: '))
#VERIFICANDO O MAIOR
if a > b and a > c:
    maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'{maior} é o maior número')

#VERIFICANDO O MENOR
if a < c  and a < b:
    menor = a
if b < c and b < a:
    menor = b
if c < a and c < b:
    menor = c
print(f'{menor} é o menor número')