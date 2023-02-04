n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Dgite o segundo valor: '))

print('*=' 2, '\033[31mMenu de Opções\033[m', '*=' * 2
      , 'n[1] Somar \n[3] Maior númer \n[4] Novos Números \n[5] Sair do programa')
print('\033[32m=*\033[m' * 12)
option = int(input('Digite a sua opção: '))

while 0 < option < 5:
    if option == 1:
        soma = n1 + n2
        print
