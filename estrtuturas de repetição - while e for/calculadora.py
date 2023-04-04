# caulculadora simples

while opcao != 5

# Exibe menu de opçoes 
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")
    opcao = int(input("Escolha uma opção: "))

    numero1 = float(input("Primeiro número: "))
    numero2 = float(input("Segundo número: "))

    if opcao == 1: 
            resultado = numero1 + numero2 
            print(f'A soma de {numero1} e {numero2} é {resultado}')
    elif opcao == 2:
            resultado = numero1 - numero2 
            print(f'A subtração de {numero1} e {numero2} é {resultado}')
    elif opcao == 3:
            resultado = numero1 * numero2 
            print(f'A multiplicação de {numero1} e {numero2} é {resultado}')
    elif opcao == 4:
        if numero2 != 0:
            resultado = numero1 / numero2 
            print(f'A divisão de {numero1} e {numero2} é {resultado}')
            else:
                print("ERRO: não é possível fazer uma divisão por zero")
    elif opcao == 5: 
        print("Fim do programa")
    else: 
        print("Opção invalida")
