#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$



hora = float(input("Quanto você ganha por hora?\n"))
horatrab = int(input("Quantas horas trabalhadas esse mês?\n"))
sal = hora*horatrab

ir = 0.11*sal
inss = 0.08*sal
sind = 0.05*sal
desc = ir+inss+sind
liqui = sal - desc


print('''Salário Bruto : R$ {:.2f}

IR (11%) : R$ {:.2f}

INSS (8%) : R$ {:.2f}

Sindicato ( 5%) : R$ {:.2f}

Salário Liquido : R${:.2f} '''.format(sal, ir, inss, sind, liqui))

