from random import choice
jokenpo = ['PEDRA','papel','TESOURA']

print('JOKEMPÔ')
print('-'*7)
print('Vamos brincar de jokenpô, escolha entre Pedra, Papel ou Tesoura.')

jogador = str(input('Escolha: ')).upper()
computador = choice(jokenpo)

if jogador == 'PEDRA' and computador == 'TESOURA' or jogador == 'PAPEL' and computador == 'PEDRA' or jogador =='TESOURA' and computador == 'PAPEL':
    print(f'{jogador} vs {computador}')
    print('VITÓTIA!')
elif jogador == 'PEDRA' and computador == 'PEDRA' or jogador == 'PAPEL' and computador == "PAPEL" or jogador == 'TESOURA' and computador == 'TESOURA':
    print(f'{jogador} vs {computador}')
    print('EMPATE')
elif jogador == 'PEDRA' and computador == 'PAPEL' or jogador == 'PAPEL' and computador == 'TESOURA' or jogador == 'TESOURA' and computador == 'PEDRA':
    print(f'{jogador} vs {computador}')
    print('DERROTA!')
else:
    print('INVÁLIDO!')

