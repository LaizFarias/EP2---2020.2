def adiciona_na_mesa(peça, mesa):

    if mesa == []:

        mesa.append(peça)

    elif peça[1] == mesa[0][0]:

        mesa.insert(0, peça)

    elif peça[0] == mesa[0][0]:

        peça.reverse()

        mesa.insert(0, peça)

    elif peça[1] == mesa[len(mesa)-1][1]:

        peça.reverse()

        mesa.append(peça)

    else:

        mesa.append(peça)

    return mesa