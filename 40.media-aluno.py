nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
m = (nota1 + nota2)/2

print(f'A média obstida pelo aluno foi {m:.2f}')

if m < 5.0:
    print('O aluno foi REPROVADO.')
elif 5.0 <= m < 6.9:
    print('O aluno ficou de RECUPERAÇÃO.')
else:
    print('O aluno foi APROVADO.')

