print('{:=^40}'.format('LOJAS A'))
preco = float(input('Preço das compras: R$'))
print('''FORMA DE PAGAMENTO:
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão''')
option = int(input('Qual é a opção?: '))

if option == 1:
    preco_final = 0.9*preco
    print(f'Pagamento com dinheiro/cheque você tem 10% de desconto. O preço final do produto será R$ {preco_final:.2f}.')
elif option == 2:
    preco_final = 0.95*preco
    print(f'O pagamento avista no cartão você tem 5% de desconto. O preço final do prosuto será R$ {preco_final:.2f}.')
elif option == 3:
    parcela = preco/2
    print(f'A sua compra será parcela em duas parcelas de R$ {parcela} SEM JURIOS.')
    print(f'Sua compra de R$ {preco:.2f} não sofrerá alteração no preço.')
elif option == 4:
    parcelas = int(input('Quantas parcelas? '))
    preco_final = 1.2*preco
    preco_mensal = preco_final/parcelas
    print(f'A sua compra será parcelada em {parcelas} parcelas de R$ {preco_mensal:.2f} COM JUROS ')
    print(f'Sua compra de R$ {preco:.2f} vai custa R$ {preco_final} no final.')