alturachico = 1.5
alturajuca = 1.1

anos = 0        #contadora 
while alturajuca <= alturachico:
    alturachico += 0.02
    alturajuca += 0.05
    anos += 1 

print(f'A quantidae de anos para que o Juca seja mais alto é {anos}')