m1 = int(input('INFORME SUA NOTA DA PRIMEIRA PROVA: '))
m2 = int(input('INFORME SUA NOTA DA SEGUNDA PROVA: '))
m = (m1 + m2) / 2
if m < 5:
    print('REPROVADO')
elif 5 <= m <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
