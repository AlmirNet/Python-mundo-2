from datetime import date
atual = date.today().year
nasc = int(input('Informe o ano de nascimento do atleta: '))
idade = atual - nasc

print(f'O atleta tem {idade} anos.')

if idade <= 9:
    print('O atleta está na categoria MIRIM.')
elif 9 < idade <= 14:
    print('O atleta está na categoria INFANTIL')
elif 14 < idade <= 19:
    print('O atleta está na categoria JUNIOR.')
elif 19 < idade <= 20:
    print('O atleta está na categoria SÊNIOR.')
else:
    print('O atleta está na categoria MASTER.')