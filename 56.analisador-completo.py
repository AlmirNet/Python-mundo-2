med = 0
mul = 0
homemid = 0
soma = 0
homemvelho = ''
for c in range(1, 4):
    print(f'\033[1m---- {c}ª Pessoa ----\033[m')
    nom = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sex = str(input('SEXO [H/M]: ')).strip()
    if c == 1 and sex in 'Hh':
        homemvelho = nom
    if sex in 'Hh' and idade > homemid:
        homemvelho = nom
    if sex in 'Mn' and idade < 20:
        mul += 1
    soma += idade
med = soma/4
print(f'O nome do homem mais velho é \033[1m{homemvelho}\033 .')
print(f'A média da idade do grupo é \033[1m{med}\033[m')
print(f'\033[1m{mul}\033[m Mulheres têm menos de 20 anos')


    