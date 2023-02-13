print ('Sequencia de fibonacci')
print ('=-' * 2)
n = int(input('Digite um número inteiro de termos: '))
cont = 1
t1 = 0
t2 = 1
t3 = 0
print(f'{t1} → {t2} → ', end='')
while cont <= n:
    t3 = t1 + t2
    print(f'{t3} → ' ,end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM!')