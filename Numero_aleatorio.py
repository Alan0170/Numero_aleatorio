from random import randint
from time import sleep
computer = randint(0,7) #Faz o computador pensar
print('-<>-' *14)
print('Vou pensar em um número entre 0 e 7. Tente advinhar...')
print('-<>-'*14)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta adivinhar
print('PROCESSANDO...')
sleep(3)
if jogador == computer:
    print('Parabéns! Você conseguiu me vencer!')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computer,jogador))