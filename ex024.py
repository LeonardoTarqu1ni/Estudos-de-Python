num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))
if num1 > num2:
    print(f'O primeiro numero é maior pois {num1} é maior do que {num2}!')
elif num1 < num2:
    print(f'O segundo numero é maior pois {num2} é maior que {num1}!')
elif num1 == num2:
    print('Não existe maior, os dois são iguais!')