#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário
print("Olá")
lado = float(input("digite a medida de um lado do quadrado: "))
area = lado*lado
dbarea = area*2
print("A area deste quadrado é {:.2f} e o dobro desta área é {:.2f}".format(area, dbarea))