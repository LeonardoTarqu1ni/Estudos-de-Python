
ano = int(input('Qual ano voce nasceu?: '))
idade = 2022 - ano
if idade == 18:
    print('Está na hora de se alistar! corra!')
elif idade > 18:
    print('Você passou da idade, vá atras da sua reservista!')
    print(f'Você está atrasado', idade - 18, 'anos')
elif idade < 18:
    print('Voce ainda não tem idade para se alistar, aguarde os 18 anos!')
    print('ainda faltam', (idade - 18) * -1)
   #(idade - 18) * -1)