n = int(input("Informe o valor de N: "))

cont = 1
soma = 0 
while cont <= n:
    soma += 1/cont
    cont +=1 

print(f'A soma é {soma}')