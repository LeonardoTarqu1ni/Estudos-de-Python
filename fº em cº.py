#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
print("Olá")
f = float(input("Quantos grau fahrenheit?"))
c = (f-32) / 1.8

print("{:.2f}ºf convertido em graus celsius fica {:.2f}cº".format(f, c))