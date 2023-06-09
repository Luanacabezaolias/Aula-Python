while True:
    print('1 - Soma')
    print('2 - Subtração')
    print('3 - multiplicação')
    print('4 - divisão')
    print('5 - Sair')
    try:
        opcao = int(input("Escolha uma opção: "))
        if opcao == 5:
            print("Fim do programa")
            break

        try:
            if opcao >= 1 and opcao <= 4:
                a = float(input("Primeiro número:"))
                b = float(input("Segundo número:"))
        except ValueError:
            print("ERRO: os valores informados não são números")
        else: 
            if opcao == 1:
                print(f'Soma: {a + b}')
            elif opcao == 2:
                print(f'Subtração: {a - b}')
            elif opcao == 3:
                print(f'Multiplicação: {a * b}')
            elif opcao == 4:
                try:
                    print(f'Divisão: {a / b}')
                except ZeroDivisionError:
                    print("ERRO; ocorreu uma divisão por zero")
            else: 
                print("Opção inválida")
    except ValueError:
        print("ERRO: Você deve digitar um valor entre 1 e 5")
    except Exception:
        print("ERRO: variável não definida")
                