nome_aluno = input('Digite o nome do Aluno:')
nota_1 = float(input('Digite a primeira nota:'))
nota_2 = float(input('Digite a segunda nota:'))
nota_final = (nota_1+nota_2)/2 # calculo da média das duas provas
media = 7
media_recuperacao = 8 # nota de recuperação
if nota_final >= media:
    print('aluno aprovado!')
else:
    print('aluno em recuperação!')
    rec = float(input('Nota da recuperação: '))
    if rec >= media_recuperacao:
        print('Aluno aprovado!')
    else:
        print('Aluno reprovado!')

print('A nota final do Aluno(a) {} foi {}'.format(nome_aluno, nota_final))
