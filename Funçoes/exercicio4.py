'''
Faça uma funçãoque recebeum número inteiro por parâmetro e retorna True se for par 
e False se for ímpar.
'''

def par_ou_impar(numero):
    if numero % 2 == 0:
        print(True)
    else:
        print(False)

numero = float(input("Informe um número: "))
par_ou_impar(numero)
