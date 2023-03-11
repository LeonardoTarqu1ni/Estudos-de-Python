print('\033[4;30;45m===========BANCO TARQUINI!===========\033[m')
nome = str(input('Digite seu nome:'))
print(f'Ola {nome}, bem vindo!')
saldo = 17000
senha = int(input(f'Digite sua senha \033[4;30;45m{nome}\033[m:' ))
if senha == 159753:
    saque = int(input('Digite o valor a ser sacado:'))
    restante = saldo - saque
    print(f'\033[1;32mO valor sacado foi: R${saque},00 , saldo atual:R${restante},00\033[m')
    print('Tenha um ótimo dia!')
else: print('\033[0;31mSenha incorreta, tente novamente!\033[m')

