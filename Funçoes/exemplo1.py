

def exibir_mensagem():
    print("Olá")

def calcuar_area_de_um_triangulo(base, altura):
    area = (base * altura) / 2
    print(f'área: {area}')
    
base = float(input('Base do trinagulo: '))
altura  = float(input('Altura do trinagulo: '))
area = calcuar_area_de_um_triangulo(base, altura)  # chamada da funçao 
    print(f'Area do triangulo {area}')

exibir_mensagem()  # chamada da funçao