import random 

def cria_pecas():
    # lista para guarda as peças; 
    pecas = []
    #gerando o primeiro lado da peça;
    for i in range(7):
        #escolhido o primeiro lado, gera o segundo lado da peça;
        # De (i,7), pq tem que excluir o elemento, não pode
        #existir peças do tipo (1,2) e (2,1) 
        for j in range(i, 7):
            #faz a peça e appenda na lista peças
            pecas.append([i, j])
    
    random.shuffle(pecas)
    return pecas
