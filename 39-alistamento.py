from datetime import date
atual = date.today().year
sexo = str(input('Informe seu sexo: ')).upper()
ano = int(input('Informe o ano de seu nascimento: '))
idade = atual-ano
print(f'Quem nasceu em {ano} tem {idade} anos em {atual}.')

if sexo == 'FEMININO':
    print('O alistamento não é obrigatório para mulheres.')

if sexo == 'MASCULINO':
    if idade < 18:
        print(f'Ainda falta {18-idade} anos o alistamento.')
        print(f'Seu alistamento será em {anos+18}.')
    elif idade == 18:
        print('Você tem que alistar IMEDIATAMENTE!')
    elif idade > 18:

        print(f'Você já deveria ter se alistado há {idade-18} anos.')
        print(f'Seu alistamento foi em {ano+18}.')

