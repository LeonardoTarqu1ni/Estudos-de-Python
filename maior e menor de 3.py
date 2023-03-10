#Faça um Programa que leia três números e mostre o maior e o menor deles.

print(">>>Olá!<<<")
n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))

if n1 > n2 and n1 > n3:
    print("{} é o maior de todos!".format(n1))

elif n3 > n1 and n3 > n2:
    print("{} é o maior de todos!".format(n3))

elif n2 > n1 and n2 > n3:
    print("{} é o maior de todos!".format(n2))

print("_______________________________")

if n1 < n2 and n1 < n3:
    print("{} é o menor de todos!".format(n1))

elif n3 < n1 and n3 < n2:
    print("{} é o menor de todos!".format(n3))

elif n2 < n1 and n2 < n3:
    print("{} é o menor de todos!".format(n2))