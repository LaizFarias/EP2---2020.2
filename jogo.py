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


def colorir(frase, cor):
    # Tabela de cores - Usadas pela função "colorir"
    BOLD    = "\033[;1m"
    RED   = "\033[1;31m"  
    BLUE  = "\033[1;34m"
    YELLOW  = "\033[1;33m"
    CYAN  = "\033[1;36m"
    GREEN = "\033[0;32m"
    RESET = "\033[0;0m"
    REVERSE = "\033[;7m"
    cores = {
        'vermelho': RED,
        'azul': BLUE,
        'ciano': CYAN,
        'amarelo': YELLOW,
        'verde': GREEN,
        'preto': BOLD,
    }
    return cores[cor] + frase + RESET


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
        frase = "As peças da mesa são: {} ".format(mesa)
        print(colorir(frase, 'azul'))
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
                        print(colorir('O jogador vencedor é : {}'.format(venceu), 'vermelho'))
                    else: 
                        print(colorir('Os jogadores que empataram foram : {}'.format(venceu), 'vermelho'))

            else: 
                print('Não há peças pra você. Pegue algo no monte!')
                mao_jogador[jogador_inicial].append(monte[0])
                del monte[0]
        else: #significa que tem peça pra ser jogada 
            if jogador_inicial == 0:

                frase = ('A suas peças são {}'.format(mao_jogador[jogador_inicial]))
                print(colorir(frase, 'amarelo'))
                
                print(colorir('A possiveis são {} '.format([mao_jogador[jogador_inicial][i] for i in posicao]), 'verde'))
                peca_para_jogar = int(input('Escolha a sua peça {}'.format(posicao))) - 1

                if (peca_para_jogar+1) not in posicao:
                    while (peca_para_jogar+1) not in posicao:
                        print('Não temos essa peça!')
                        peca_para_jogar = int(input('Escolha a sua peça {}'.format(posicao))) - 1


            else:
                peca_para_jogar = random.randint(0,len(posicao)-1) # as duas linhas atualizam a mesa com a peça da mao do jogador da vez, na posição da peça a ser jogada. 
                peca_para_jogar = posicao[peca_para_jogar]

            mesa = adiciona_na_mesa(mao_jogador[jogador_inicial][peca_para_jogar],mesa) 
            del mao_jogador[jogador_inicial][peca_para_jogar]
            if len(mao_jogador[jogador_inicial]) == 0: 
                estado = False 
                print(colorir('fim de jogo, quem venceu foi o jogador {}'.format(jogador_inicial), 'vermelho'))
            else:
                jogador_inicial  = proximo_player(numero,jogador_inicial)

    comeca = input("Você quer jogar? (sim/não)").strip().lower()
