'''
Escreva um algoritmo que solicite um número inteiro e exiba todos os divisores desse número.
'''

numero = int(input("Número: "))

for n in range(1, numero+1):
    if numero % n == 0:
        print(n)