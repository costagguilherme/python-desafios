frase = str(input('Digite uma frase qualquer: ')).strip().upper()
a = frase.count('A')
print(f'A letra A aparece {a} vezes na frase')
b = frase.find('A')
print(f'A letra A aparece na frase pela primeira vez na posição {b}')
c = frase.rfind('A')
print(f'A letra A aparece pela última na posição {c}')