while True:
    print()
    num_1 = input('Digite um número: ')

    if not num_1.isnumeric():
        print('Você precisa digitar um número.')
        continue
    elif num_1.isnumeric():
        print()
        operador = input('Digite um operador: ')
        if operador not in '+ - * /':
            print('Você precisa digitar um operador válido:')
            continue

        else:
            print()
            num_2 = input('Digite outro número: ')

            if not num_2.isnumeric():
                print('Você precisa digitar um número.')
                continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    if operador == '+':
        resultado = (num_1 + num_2)
        print(f'O resultado é {resultado}.')
    elif operador == '-':
        resultado = (num_1 - num_2)
        print(f'O resultado é {resultado}.')
    elif operador == '/':
        resultado = (num_1 / num_2)
        print(f'O resultado é {resultado}.')
    elif operador == '*':
        resultado = (num_1 * num_2)
        print(f'O resultado é {resultado}.')


    print()
    sair = input('Deseja sair? [S]im ou [N]ão: ')

    if sair == 's':
        break