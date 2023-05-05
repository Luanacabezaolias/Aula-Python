'''
Faça  um  programa  para  uma  calculadora  simples  com  as  seguintes  operações:
 adição,  subtração, multiplicação e divisão.
 O programa começa apresentando ao usuário um menu de opções semelhante ao mostrado abaixo:
'''
# Definindo Funções


def menuOpcoes():

         print("Bem vindo(a) à Calculadora Python! \n Escolha uma opção abaixo:")

         print("1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Sair do programa")


         opcao = int(input("Informe uma opção: "))

         return opcao


def funcaoAdicao(num1, num2):


         adicao = num1 + num2

         print(adicao)


def funcaoSubtracao(num1, num2):


        subtracao = num1 - num2

        print(subtracao)


def funcaoMultiplicacao(num1, num2):


         multiplicacao = num1 * num2

         print(multiplicacao)


def funcaoDivisao(num1, num2):


         divisao = num1 / num2

         print(divisao)


while True:

 '''
Armazeno o valor da função dentro de uma variável, pois, se eu chamar a função em cada

condição, o programa vai executar todas as vezes até confirmar qual condição é a correta!

'''

        opcao = menuOpcoes()

         if opcao == 1:

                 num1 = float(input("Informe o primeiro número: "))

                 num2 = float(input("Informe o segundo número: "))

                 funcaoAdicao(num1, num2)
         elif opcao == 2:

                 num1 = float(input("Informe o primeiro número: "))

                 num2 = float(input("Informe o segundo número: "))

                 funcaoSubtracao(num1, num2)
         elif opcao == 3:

                 num1 = float(input("Informe o primeiro número: "))
                
                 num2 = float(input("Informe o segundo número: "))

                 funcaoMultiplicacao(num1, num2)

         elif opcao == 4:

                 num1 = float(input("Informe o primeiro número: "))
                
                 num2 = float(input("Informe o segundo número: "))

                 funcaoDivisao(num1, num2)

         elif opcao == 5:

                 print("Finalizando a calculadora...")

                 break

         else:

                 print("Opção inválida, por favor, tente novamente.")
