'''
Escreva um algoritmo que determine se um número N (digitado pelo usuário) é primo ou não.
'''

numero = int(input("Número: "))

cont = 0
for n in range(2, numero):
    if numero % n == 0:
        cont += 1

if cont == 0 and numero != 1: 
    print("Primo")
else:
    print("Não é Primo")