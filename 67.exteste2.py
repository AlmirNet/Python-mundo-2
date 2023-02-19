while True:
    n = int(input('Você quer ver tabuada de qual valor: '))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} X {c} = {n*c}')
print('PROGRAMA DE TABUADA ENCERRADO,É MUITO AGRADAVEL!')
