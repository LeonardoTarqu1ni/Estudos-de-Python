#Faça um Programa que leia um número e exiba o dia correspondente da semana.
# (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print("Olá!")
print('''
Digite um número que represente o dia de hoje: 
exemplo:
[1] DOMINGO
[2] SEGUNDA
[3] TERÇA
[4] QUARTA
[5] QUINTA
[6] SEXTA
[7] SÁBADO
''')
dia = int(input("hoje é que dia da semana?\n"))

if dia == 1:
    print("hoje é domingo!")
elif dia == 2:
    print("hoje é segunda!")
elif dia == 3:
    print("hoje é terça!")
elif dia == 4:
    print("hoje é quarta!")
elif dia == 5:
    print("hoje é quinta!")
elif dia == 6:
    print("hoje é sexta!")
elif dia == 7:
    print("hoje é sábado!")
else:
    print("numero da semana inválido, tente novamente!")
