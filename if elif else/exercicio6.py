horas = int(input("Iforme as horas: "))
minutos = int(input("Iforme os minutos: "))

if horas >= 0 and horas <= 23 and minutos >= 0 and minutos <= 59:
    print("Horas e minutos validos")
else:
    print("Horas e minutos invalidos")

# ou 
if horas < 0 or horas > 23 or minutos < 0 or minutos > 59:
    print("Invalido")
else: 
    print("Valido")
    