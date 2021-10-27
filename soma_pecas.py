def soma_pecas(jogo):
    pontos = 0
    for peca in jogo: 
        pontos += sum(peca)
    return pontos