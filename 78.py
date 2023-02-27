number = []
for count in range(5):
    number.append(int(input(f'Digite o {count + 1} número: ')))
print('+=' * 30)
print(f'Você digitou os valores {number}')