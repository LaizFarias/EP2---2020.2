def verifica_ganhador(numero_jogadores):
    for jogador in numero_jogadores:
        if numero_jogadores[jogador] == []:
            return jogador 

    return -1 