def posicoes_possiveis(mesa,pecas):
    #guarda as posições da pea na lista de peças 
    posicoes = []
    #verifica se a mesa é vazia 
    if mesa == []: 
        i = 0
        #se a mesa for vazia , todas as posições da lista de peças são validas 
        while i < len(pecas):
            posicoes.append(i)
            i += 1 

    else:
        #peças a serem analisadas serão as peças da ponta da mesa
        pecas_ponta =[mesa[0][0], mesa[len(mesa)-1][1]]
        #checa as peças existentes
        for i in range(len(pecas)): 
            # ver se um dos lados está nas peças da ponta 
            if (pecas[i][0] in pecas_ponta) or pecas[i][1] in  pecas_ponta:
                posicoes.append(i)
    return posicoes