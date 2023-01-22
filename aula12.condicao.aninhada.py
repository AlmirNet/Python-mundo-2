nome = str(input('Qual é seu nome? '))
if nome == 'Almir':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Stefhany' or nome == 'João':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Lucia de Amaro':
    print('Belo nome femino')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia,{nome}')