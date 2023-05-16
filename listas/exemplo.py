# preencha uma lista 
lista = []
for i in range(10):      # preenche uma lista com 10 números
    numero = int(input("Número: "))
    lista.append(numero)

print(lista)

# percorrer os itens da lista
cont = 0 
for item in lista:
    if item % 2 == 0:
        cont += 1 

print(f'Quantidade de números pares: {cont}')
