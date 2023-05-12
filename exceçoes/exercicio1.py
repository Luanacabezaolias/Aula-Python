'''
Crie uma função que receba três números como parâmetros, e retorne True 
se a soma de quaisquer pares de números gera a soma do terceiro número. 
Caso contrário retorne False.
'''
def somanum(a, b, c):
    if a + b == c or b + c == a or a + c ==b:
        return True
    else:
        return False

while True:
    try:
        a = float(input("primeiro valor: "))
        b = float(input("segundo valor: "))
        c = float(input("terceiro valor: "))
        resultado = somanum(a, b , c)
        print(resultado)
    except ValueError:
        print("Erro: os valores informados não são números")
    else:
        print("O programa foi finalizado")
        break



    

