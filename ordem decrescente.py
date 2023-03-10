#Faça um Programa que leia três números e mostre-os em ordem decrescente.

n1 = float(input("Digite um numero: "))
n2 = float(input("Digite outro número: "))
n3 = float(input("Digite mais um número: "))

if n1 >= n2 and n1 >= n3 and n2 >= n3:
    print("A ordem decrescente é: {}, {} e {}".format(n1, n2, n3))
elif n1 >= n2 and n1 >= n3 and n3 >= n2:
    print("A ordem decrescente é: {}, {} e {}".format(n1, n3, n2))
elif n2 >= n1 and n2 >= n3 and n1 >= n3:
    print("A ordem decrescente é {} , {} e {}".format(n2, n1, n3))
elif n2 >= n1 and n2 >= n3 and n3 >= n1:
    print("A ordem decrescente é {} , {} e {}".format(n2, n3, n1))
elif n3 >= n1 and n3 >= n2 and n1 >= n2:
    print("A ordem decrescente é {} , {} e {}".format(n3, n1, n2))
elif n3 >= n1 and n3 >= n2 and n2 >= n1:
    print("A ordem decrescente é {} , {} e {}".format(n3, n2, n1))
