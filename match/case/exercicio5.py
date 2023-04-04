print("1 - Picanha - 25,00") 
print("2 - Lasanha - 20,00")
print("3 - Strogonoff - 20,00")
print("4 - Bife Acebolado - 15,00")
print("5 - Pão com Ovo - 5,00")

opcao = int(input("Escolha o pato desejado: "))

match opcao:
    case 1:
        valor = 25.00
    case 2:
        valor = 20,00
    case 3:
        valor = 20.00
    case 4:
        valor = 15.00
    case 5:
        valor = 5.00
    case _:
        print("Opção inválida")

gorjeta = input("Deseja pagar os 0 (sim/não): ")
match gorjeta:
    case 'sim':
        valor = valor + valor * 10/100
        print(f'Valor total: {valor}')
    case 'não':
        print(f'Valor total: {valor}')
