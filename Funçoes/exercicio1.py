'''
Escreva  um  programa  para solicitaras  notas  de  duas provas. 
Faça  umafunçãoque  receba  as  duas notas por parâmetro e exibe a mensagem “Você foi Aprovado!”
ou “Você foi Reprovado!”. Considere 6.0 a média mínima para aprovação.
'''
def aprovacao(nota1, nota2):
    media = (nota1 + nota2) / 2
    print(f"A sua media foi {media}")
    if media >= 6:
        print("Você foi aprovado")
    else:
        print("Você foi reprovado")

nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
aprovacao(nota1, nota2)    # chamada da função