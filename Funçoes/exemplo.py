def exibir_mensagem():
    print("Olá")

def calcuar_area_de_um_triangulo(base, altura):
    area = (base * altura) / 2
    print(f'área: {area}')

def par_ou_impar(numero):
     if numero % 2 == 0:
         print("Par")
     else:
         print("Impar")
 
while True:
    print('1 - Exibir uma mensagem')
    print('2 - Verificar se o número é par ou ímpar')
    print('3 - calcular a área do triangulo')
    print('4 - Finalizar')
    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        exibir_mensagem()
    elif opcao == 2:
        numero = int(input("Informe um número: "))
        par_ou_impar(numero)
    elif opcao == 3:
        base = float(input("Base do triangulo: "))
        altura = float(input("Altura do tiangulo: "))
        calcuar_area_de_um_triangulo(base, altura)
    elif opcao == 4:
       print("Fim da execução")
       break




