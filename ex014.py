from random import choice
aluno1 = str(input('primeiro aluno:'))
aluno2 = str(input('segundo aluno:'))
aluno3 = str(input('terceiro aluno:'))
aluno4 = str(input('quarto aluno:'))
lista = [aluno1, aluno2, aluno3, aluno4]
choice(lista)
print('Aluno que ira apagar o quadro')
print(choice(lista))