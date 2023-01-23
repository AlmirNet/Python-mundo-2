peso = float(input('Informe um peso em kg: '))
altura = float(input('Informe sua altura em metros: '))

IMC = peso/(altura**2)
print(f'seu índice de Massa Corpórea é {IMC:.2f} portanto você está', end='')

if IMC < 18.5:
    print(f' Abaixo do Peso.')
elif 18.5 <= IMC < 25: 
    print(' no peso Ideal, exercite o corpo para melhorar.')
elif 25 <= IMC < 30:
    print(' com sobrepeso.')
elif 30 <= IMC < 40:
    print(' com Obesidade.')
else:
    print(' com Obesidade Mórbida.')