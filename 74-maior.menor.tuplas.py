from random import randint
# a = tuple(randint(0, 100) for c ranger(5))
# Gera uma lista dos números de 1 a 100.
# b = tuple(i for i in range(1,101))
# print(a)
# print(b)
numbert = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100),)
print(f'Lista de números gerada: {numbert}')
print(f'Menor valor: {sorted(numbert)[0]} \nMaior valor: {sorted(numbert)[-1]}')
