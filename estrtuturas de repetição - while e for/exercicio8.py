cont = 1

num = int(input('insira um número: '))

menor = num

while cont <= 9:

    num = int(input('insira um número: '))

if num < menor:

     menor = num
     cont += 1

print(menor)





