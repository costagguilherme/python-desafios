a = ('FLAMENGO', 'ATLÉTICO PR', 'GRÊMIO', 'SANTOS', 'PALMEIRAS',
     'FORTALEZA', 'SÃO PAULO', 'GOIÁS', 'FLUMINENSE', 'VASCO',
     'CORINTINHAS', 'INTER', 'ATLÉTICO MG', 'BAHIA',
     'CHAPECOENSE', 'CRUZEIRO', 'PONTE PRETA', 'BOTAFOGO', 'REMO', 'AVAÍ')

print(f'5 PRIMEIROS COLOCADOS: {a[0:5]}')
print('-='*30)
print(f'4 ÚLTIMOS = {a[16:]} ')
print('-='*30)
print(f'TIMES EM ORDEM ={sorted(a)}')
print('-='*30)
print(f'O TIME CHAPECONESE ESTÁ NA {a.index("CHAPECOENSE")}° POSIÇÃO')
