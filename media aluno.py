print("Olá")
esc = input("Qual o nome da escola?\n")
aluno = input("Qual o nome do aluno?\n")
media = float(input("Qual a média de aprovação?\n"))
n1 = float(input("Qual a primeira nota desse aluno?\n"))
n2 = float(input("Qual a segunda nota desse aluno?\n"))
nf = (n1+n2)/2
print("nota final do aluno foi", nf);
if nf < media:
        print("aluno reprovado")

else:
    print("O aluno {} foi aprovado".format(aluno))