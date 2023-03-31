salario = float(input("Informe o salário do vendedor: "))

if salario <= 1500: 
    aumento = salario * 3/100
    total = salario + aumento 
    print(f'Salário final: {total}')
    