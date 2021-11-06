from adiciona_na_mesa import *
from cria_pecas import * 
from inicia_jogo import *
from posicoes_possiveis import * 
from soma_pecas import * 
from verifica_ganhador import * 
from proximo_player import *
import random 

print("\nInsper Dominó ")
print("\n=> Design de Software ")

print("\nBem-vindo(a) ao jogo de Dominó! O objetivo desse jogo é ficar sem peças na sua mão antes dos outros jogadores. ")

print("\nVamos começar!!!")




comeca = input("Você quer jogar? (sim/não)").strip().lower()

while comeca not in "não":
    dominos =  cria_pecas()
    numero = int(input("Quantos jogadores? (2~4)"))
    distribui = inicia_jogo(numero,dominos)
    mesa = distribui['mesa']
    monte = distribui['monte']
    jogador_inicial =  random.randint(0,numero - 1)
    mao_jogador = distribui['jogadores']
    empate = 0 
    soma_pontos = []
    venceu = [] 
    estado = True
    while estado : 
        #posições possiveis do jogador da vez 
        posicao = posicoes_possiveis(mesa,mao_jogador[jogador_inicial])
        #checa se precisa do monte 
        print("As peças da mesa são: {} ".format(mesa))
        if posicao ==  []:
            if monte == []: #se o monte estiver vazio incrimenta o empate
                print('Que pena, não tem peça no monte!')
                jogador_inicial  = proximo_player(numero,jogador_inicial)
                empate += 1
                if empate == numero:
                    estado = False 
                    for jogador in mao_jogador: 
                        soma_pontos.append(soma_pecas(mao_jogador[jogador]))

                    ganhador = min(soma_pontos)  

                    for jogador in mao_jogador: 

                        if soma_pontos[jogador] == ganhador:
                            venceu.append(jogador+1)
                    if len(venceu) == 1: 
                        print('O jogador vencedor é : {}'.format(venceu))
                    else: 
                        print('Os jogadores que empataram foram : {}'.format(venceu))
