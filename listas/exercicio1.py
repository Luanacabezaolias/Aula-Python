'''
Solicite 10 números inteiros ao usuário e armazene os números pares em uma lista,
e os números ímpares em outra lista.Exiba as duas listas ao usuário.
'''
lista = []
for i in range(10):      # preenche uma lista com 10 números
    numero = int(input("Número: "))
    lista.append(numero)

print(lista)


