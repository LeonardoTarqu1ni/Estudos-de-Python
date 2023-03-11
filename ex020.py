velocidade = float(input('Qual a velocidade do carro?: '))
multa = (velocidade-80) * 7
if velocidade > 80:
    print('MULTADO! Você excedeu a velocidade da via que é de 80 km/h, multa no valor de R${}'.format(multa))
print('Tenha um bom dia!')