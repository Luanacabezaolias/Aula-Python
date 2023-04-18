n = int(input("Informe a quantidade de números: "))

cont = 1 
somapar = 0 
somaimpar = 0 
contapar = 0 
contaimpar = 0

while cont <= n:
    numero = int(input("Número: "))
    if numero % 2 == 0:
        somapar += numero     # somatoria dos pares
        contapar += 1         # conta a quantidade dos pares 
    else:
        somaimpar += numero   # somatorio dos impares 
        contaimpar += 1       # conta a quantidade de impares 
    cont += 1

if contapar > 0:
    mediapar = somapar / contapar
    print(f'A mmedia dos pares: {mediapar}')
else: 
    print(f'Não há números pares')

if contaimpar > 0:
    mediaimpar = somaimpar / contaimpar
    print(f'A mmedia dos impares: {mediaimpar}')
else:
    print(f'Não há números impares')
