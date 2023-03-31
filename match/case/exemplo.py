opcao = int(input("Escolha uma opção: "))

match opcao:
    case 1:
        print ("Opção1")
    case 2 | 3:
        print("Opção 2 ou Opção 3")
    case _ :
        print("Nenhuma das opções anteriores")

 # or = |
 # case _ = else