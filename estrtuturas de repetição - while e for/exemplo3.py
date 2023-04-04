'''
Solicitar para o usuário 10 números e informar quantos desses números são pares 
'''

cont = 1 
contapar = 0 
while cont <= 10:
    numero = int(input("Informe um número: "))
    if numero  % 2 == 0:
        contapar +=1     #contador dos pares 
    cont += 1            #contador das repetições 
print(f'quantidade de par: {contapar}')
