'''
Faça uma funçãoque receba como parâmetro o número de lados de um polígono e:
-Se o número de lados for igual a 3, escrever TRIÂNGULO.
-Se o número de lados for igual a 4, escrever QUADRILÁTERO.
-Se o número de lados for igual a 5, escrever PENTÁGONO.
-Se o número de lados for diferente de 3, 4 ou 5, escrever VALOR INVÁLIDO.
'''
def numero_de_lados(lados):
    if lados== 3:
        print (f'Triângulo')
    elif lados == 4:
        print (f'Quadrilátero')
    elif lados == 5:
        print (f'Pentágono')
    else:
        print (f'Valor Inválido')
    
lados = int(input("Número de lados: "))
numero_de_lados(lados)
