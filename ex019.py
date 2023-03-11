from random import randint
from time import sleep
computador = randint(0, 5) #faz o computador "pensar"
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
jogador = int(input('Em que numero eu pensei?: ')) #tente advinhar
print ('PROCESSANDO...')
sleep (1)
if jogador == computador:
    print('PARABENS! Voce conseguiu me vencer!')
else:
    print('Ganhei eu pensei no numero {} e não no numero {}'.format(computador, jogador))

