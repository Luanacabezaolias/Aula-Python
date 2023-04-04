cont = 1 
a = 0 
while cont <=15:
    idade = int(input("Insira sua idade: "))
    if idade < 18: 
        a += 1 
    cont += 1
print(f'A quatidade de pessoas com idade menor que 18 é {a}')
    
