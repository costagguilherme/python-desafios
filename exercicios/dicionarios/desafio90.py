nome = str(input('INFORME O NOME DO ALUNO: '))
media = int(input('INFORME A MÉDIA: '))
info = {}
info['Nome'] = nome
info['Média'] = media
print(f'NOME: {info["Nome"]}')
print(f'MÉDIA: {info["Média"]}')
if info["Média"] >= 7:
    print('APROVADO')
else:
    print('REPROVADO')