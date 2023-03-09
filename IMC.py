#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
print("Seja bem vindo(a)!")
altura = float(input("Qual sua altura?(ex: 1.75)\n"))
sx = 0
print("Qual seu sexo?")
print('''[1] MASCULINO
[2] FEMININO''')
sx = int(input("sexo:"))

if sx == 1:
    pim = (72.7 * altura) - 58
    print("Seu peso ideal é {:.2f}.".format(pim))

elif sx == 2:
    pif = (62.1 * altura) - 44.7
    print("Seu peso ideal é {:.2f}.".format(pif))

else:
    print("sexo não corresponde")
print("fim do programa!")
