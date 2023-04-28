'''
Escreva um algoritmo que solicite o valor de N e calcule o fatorial de N.
'''

numero = int(input("Número: "))

fatorial = 1
for n in range(numero, 0, -1):
    fatorial *= n 

print(f'Fatorial de {numero} é {fatorial}')
