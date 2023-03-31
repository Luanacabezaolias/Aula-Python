letra = input("Informe uma letra: ")

letra = letra.lower()

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print('Vogal')

else: 
    print('Consoante')

# ou 

vogais = 'aieouAEIOU'

if letra in vogais:
    print('Vogal')
else: 
    print('Consoante')