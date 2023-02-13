n = 0
som = 0
dig = 0
while n != 999:
    n = int(input('Digite um número inteiro, exceto 999: '))
    som += n
    dig += 1
    if n == 999:
            #Desconsideração do 999
            dig -= 1
            som -= n
print(f'Foram digitados {dig} números(s) e a soma total é: {som}')