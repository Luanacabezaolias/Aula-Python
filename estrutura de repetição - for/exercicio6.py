'''
Criar um algoritmo que leia dez números inteiros e informe o maior e o menor número.
'''

numero = int(input("Informe um número: "))
menor = numero 
maior = numero
 
for i in range(9):
    numero = int(input("Informe o número: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero2

print(f'Maior: {maior}')
print(f'Menor: {menor}')