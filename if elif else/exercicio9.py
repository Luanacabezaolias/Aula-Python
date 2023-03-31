lado1 = float(input("Primeiro lado: "))
lado2 = float(input("Segundo lado: "))
lado3 = float(input("Terceiro lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("Equilatero")
elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
    print("Isósceles")
else: 
    print("Escaleno")