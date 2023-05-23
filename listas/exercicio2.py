'''
Preencha uma lista com 10 números inteiros digitados pelo usuário e exiba:
a.A média aritmética dos números armazenadosna lista.
b.O somatório dos números pares armazenados na lista.
'''

lista = []
cont = 0
while cont < 10: # lista com 5 itens
    try:
        numero = int(input('Informe um Número: '))
        lista.append(numero)
        cont += 1
    except ValueError:
        print("ERRO. O valor digitado deve ser inteiro")
print(lista)

# A média aritmética dos números armazenadosna lista. 
soma = 0 
for item in lista:
    soma += item
media = soma / len(lista)
print(f'Media da lista: {media}')

# O somatório dos números pares armazenados na lista.
soma = 0 
for item in lista:
    if item % 2 == 0:
        soma += item
print(f'Somatório dos números pares: {soma}')

