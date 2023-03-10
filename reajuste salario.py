#As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
#programa que calculará os reajustes.
#Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
#baseado no salário atual:
#salários até R$ 280,00 (incluindo) : aumento de 20%
#salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
#o salário antes do reajuste;
#o percentual de aumento aplicado;
#o valor do aumento;
#o novo salário, após o aumento.

sal = float(input("Qual o salario do colaborador?"))
if sal <= 280:
    aumento = (sal*0.20)+sal
    porc = aumento-sal
    print('''
    Salário antes do rejuste é R$ {:.2f}.
    O aumento foi de 20% (R${:.2f})
    O novo salário, após o aumento é R${:.2f}'''.format(sal, porc, aumento))
elif sal >= 281 and sal <= 700:
    aumento = (sal*0.15)+sal
    porc = aumento-sal
    print('''
    Salário antes do rejuste é R$ {:.2f}.
    O aumento foi de 15% (R${:.2f})
    O novo salário, após o aumento é R${:.2f}'''.format(sal, porc, aumento))
elif sal >= 701 and sal <= 1500:
    aumento = (sal*0.10)+sal
    porc = aumento-sal
    print('''
    Salário antes do rejuste é R$ {:.2f}.
    O aumento foi de 10% (R${:.2f})
    O novo salário, após o aumento é R${:.2f}'''.format(sal, porc, aumento))
elif sal >= 1501:
    aumento = (sal*0.05)+sal
    porc = aumento-sal
    print('''
    Salário antes do rejuste é R$ {:.2f}.
    O aumento foi de 5% (R${:.2f})
    O novo salário, após o aumento é R${:.2f}'''.format(sal, porc, aumento))
