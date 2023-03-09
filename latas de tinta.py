#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
#Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de
# 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

print("Seja bem vindo!")
m2 = int(input("Quantos m² serão pintados?\n"))
m2p = m2/3
arred = (round(m2p))
ptinta = 80*arred
print(">>>ATENÇÃO: O numero de latas foi arredondado para cima, devido a lata ser vendida somente lacrada!<<<")
print(">>>{} latas serão o suficiente para seu orçamento , o valor total é de R${}<<<".format(arred, ptinta))