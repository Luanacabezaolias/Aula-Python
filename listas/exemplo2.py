def busca(lista, item):
    for n in lista:     # percorrendo itens da lista
        if n == item:      # verifica se o valor é o que está sendo buscando
            return True
    return False        # se nao encontrar o valor retorna falso

# preencher uma lista 
lista = []
while True:
    n = int(input("Informe um número inteiro: "))
    if n == 0:
        break
    lista.append(n)
print(lista)

item = int(input("Infome um número para buscar na lista: "))
if  (busca(lista, item)):    # chama a função
    print("O número está contido na lista")
else:
    print(f'O número {item} não está contido na lista')
 

