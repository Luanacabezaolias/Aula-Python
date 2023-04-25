'''
Solicite a quantidade de alunos de uma turma e a quantidade de notas. 
Para cada aluno, solicite as suas notas e exiba a sua respectiva média
(a média deve ser arredondada para duas casas decimais).
'''
alunos = int(input('Insira a quantidade de alunos: '))
notas =  int(input('Insira a quantidade de notas: '))

for i in range(alunos):
    soma = 0
    for i in range(notas):
        n = float(input("Insira a nota: "))
        soma += n
    media = soma / notas
    print(f'Média: {round (media, 2)}')
