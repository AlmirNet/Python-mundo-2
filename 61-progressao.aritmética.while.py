a1 = int(input('DIGITE O PRIMEIRO TERMO: '))
r = int(input('DIGITE A RAZÃO: '))
term = a1
cont = 1
while cont <= 10:
    print('{} → '.format(term), end='')
    term += r
    cont += 1
print('FIM')