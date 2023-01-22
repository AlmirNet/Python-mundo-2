valor = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe seu salário: R$'))
ano = int(input('Quantos anos de financiamento? : '))

prestacao = valor/(ano*12)
print(f'Para pagar uma casa de R${valor:.2f} em {ano} anos, a prestação será de R${prestacao:.2f}')

if prestacao > 0.3*salario:
    print('EMRPÉSTIMO NEGADO')
else:
    print('EMPRESTIMO APROVADO')