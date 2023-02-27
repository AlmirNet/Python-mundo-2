number = []
mai = 0
men = 0
for c in range(0,5):
    number.append(int(input(f'Digite um valor {c}: ')))
    if c == 0:
        mai = men = number[c]
    else:
        if number[c] > mai:
            mai = number[c]
        if number[c] < men:
            men = number[c]

print('=-' * 30)
print(f'Você digitou os valores {number}')
print(f'Menor valor: {men}')
print(f'Maior valor: {mai}')