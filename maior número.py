#Faça um Programa que peça dois números e imprima o maior deles.

print(">>>>Olá!<<<")
num1 = float(input("Digite um número: "))
num2 = float(input("Digite outro número: "))
if num1 > num2:
    print("{:.2f} é maior que {:.2f}.".format(num1, num2))

elif num1 < num2:
    print("{:.2f} é maior que {:.2f}.".format(num2, num1))

elif num1 == num2:
    print("você digitou dois numeros iguais.")


