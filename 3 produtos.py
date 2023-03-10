#Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar,
#sabendo que a decisão é sempre pelo mais barato.

print(">>>Olá!<<<")
print("Qual o valor da roupa?")
m1 = float(input("Digite o preço da primeira marca (R$): "))
m2 = float(input("Digite o preço da segunda marca (R$): "))
m3 = float(input("Digite o preço da terceira marca (R$): "))

if m1 < m2 and m1 < m3:
    print("R${:.2f} é o mais barato, compre esse!!".format(m1))

elif m3 < m1 and m3 < m2:
    print("R${:.2f} é o mais barato, compre esse!!".format(m3))

elif m2 < m1 and m2 < m3:
    print("R${:.2f} é o mais barato, compre esse!!".format(m2))