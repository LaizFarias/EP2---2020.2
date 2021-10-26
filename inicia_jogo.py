def inicia_jogo(quantidade_jogadores,domino):
    distribuicao = {'jogadores': {}}

    i = 0 
    while i < quantidade_jogadores:
        # distribui as 7 primeiras peças da lista de domino para o jogador. 
        distribuicao['jogadores'][i] = domino[0:7]
        # após a distribuição exclui essas peças da lista de domino 
        del domino[0:7]
        i += 1 
    #Após distribuir todas as peças para a quantidade de jogadores dada, o que sobra na lista de domino é o  monte 
    distribuicao['monte'] = domino

    distribuicao['mesa'] = [] 

    return distribuicao