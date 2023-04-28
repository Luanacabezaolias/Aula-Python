# solicitar ao usuário vários números até que ele digite 0 

while True:  # loop infinito
    n = int(input("Número: "))

    if n == 0:
        break
    if n % 2 == 0:
        print("Par")
    else: 
        print("Ímpar")