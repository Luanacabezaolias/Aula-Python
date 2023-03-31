numero1 = float(input("Primeiro número: "))
numero2 = float(input("Segundo número: "))

print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = int(input("Escolha uma opção: "))


# verifica a opção escolhia
match opcao: 
    case 1:
        resultado = numero1 + numero2
        print(f'A soma de {numero1} e {numero2} é {resultado}')
    case  2:
        resultado = numero1 - numero2
        print(f'A subtração de {numero1} e {numero2} é {resultado}')
    case 3: 
        resultado = numero1 * numero2
        print(f'A multiplicação de {numero1} e {numero2} é {resultado}')
    case 4:
        if numero2 != 0: 
            print(f'A divisão de {numero1} e {numero2} é {resultado}')
        else:
            print("ERRO: não é possível fazer uma divisão por 0")
    case _ :
        print("Opção inválida")











