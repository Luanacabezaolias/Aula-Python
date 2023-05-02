'''
Crie uma função que recebe como parâmetro um número inteiro e retorna o seu dobro.
'''
def dobro_numero(numero):
    dobro = numero * 2 
    print(f'o dobro de {numero} é {dobro}')

numero = float(input("Informe um número: "))
dobro_numero(numero)