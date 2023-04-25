'''
Escreva um algoritmo que leia quinze números informados pelo usuário e exiba a raiz quadrada de cada número
 (Dica: utilize a biblioteca math)
'''
import math
for i in range (15):
    num = int(input("Insira um número: "))
    n = math.sqrt(num)
    print(n)

