'''
Escreva  um  algoritmo  que  exiba  20  números  aleatórios  sorteados  entre  1  e  50  
(Dica:  utilize  a biblioteca random).
'''
import random

for n in range(20):
    numero = random.randint(1, 50)
    print(numero, end=' ')