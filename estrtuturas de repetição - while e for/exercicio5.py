cont = 1 
contimpar = 0 
while cont <= 15:
    numero = int(input("Informe um número: "))
    if numero  % 2 != 0:
        contimpar +=1     #contador dos impares
    cont += 1            #contador das repetições 
print(f'quantidade de impar: {contimpar}')