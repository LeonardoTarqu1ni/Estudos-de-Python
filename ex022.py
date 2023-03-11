nome = str(input('Qual é o seu nome?'))
if nome == 'Leonardo':
    print('Que nome lindo!')
elif nome == 'Dan' or nome== 'Neto' or nome == 'Art':
    print(f'gostei, {nome}! ')
elif nome in 'Xuia':
    print(f'Linda {nome}')
else:
    print('Seu nome é padrão!')
print(f'Tenha um bom dia, {nome}!')