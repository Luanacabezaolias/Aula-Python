cont = 1 
a = 0 
while cont <= 10:
    numero = int(input("Insira um número: "))
    if numero > 100 and numero < 200:
        a += 1 
    cont += 1
print(f'Existem {a} números entre 100 e 200')