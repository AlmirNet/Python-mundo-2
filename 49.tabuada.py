print('=*' *30, '\033[m')
numero = int(input('Insira um número: '))
print('\033[31m=*' * 50, '\033[m')
print(f'Tabuada do \033[m{numero}')
print('=*' * 50, '\033[m')
cont = 0
for c in range (1, 11):
    cont = cont + 1
    conta = numero * cont
    print(f'{numero} \033[31mx {cont} \033[m=\033[35m{conta}\033[m')
print('=*' *50, '\033[m')