def proximo_player(numero_jogadores,jogador_atual):
    if jogador_atual == (numero_jogadores - 1):
        return 0
    else:
        return jogador_atual + 1