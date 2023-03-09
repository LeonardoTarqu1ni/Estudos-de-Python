#Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever:
# F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input("Qual seu sexo biológico? (F - FEMININO, M - MASCULINO?)\n"))
if sexo == ("F"):
    print("Sexo feminino!")
elif sexo ==("M"):
    print("Sexo masculino!")
else:
    print("Sexo inválido!")

