resp = 'S'
soma = quant = média = 0
while resp in 'Ss':
    núm = int(input('Digite um número: '))
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
        if núm > maior:
            maior = núm
        if núm < menor:
            menor = núm
    resp = str(input('Quer continuar? [S/N]' )).upper().strip()[0]
média =  soma / quant
print(F'Você digitou {quant} números e a média foi {média}.')
print(f'O maior valor foi {maior}, e o menor foi {menor}')  

