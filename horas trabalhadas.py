#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
print("Olá")
vh = float(input("Quando você recebe por hora trabalhada?"))
ht = float(input("Quantas horas trabalhadas por dia?"))
dt = int(input("Quantos dias trabalhados?"))

horasmes = dt*ht
salario = horasmes*vh

print("você trabalhou {:.2f} horas este mes, e seu salario foi de {:.2f}".format(horasmes, salario))
