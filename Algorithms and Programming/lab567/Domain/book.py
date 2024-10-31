def createBook(id, titlu, genCarte, pret, tipReducere):
    '''
    Subprogramul care creeaza entitatea "carte"
    :param id: id-ul cartii
    :param titlu: titlul cartii
    :param genCarte: genul cartii
    :param pret: pretul cartii
    :param tipReducere: tipul de reducere al cartii
    :return: cartea
    '''
    return (id, titlu, genCarte, pret, tipReducere)


def getId(carte):
    '''
    Determina id-ul cartii
    :param carte: cartea
    :return: id-ul cartii
    '''
    return carte[0]


def getTitle(carte):
    '''
    Determina titlul cartii
    :param carte: cartea
    :return: titlul cartii
    '''
    return carte[1]


def getBookType(carte):
    '''
    Determina genul cartii
    :param carte: cartea
    :return: genul cartii
    '''
    return carte[2]


def getPrice(carte):
    '''
    Determina pretul cartii
    :param carte: cartea
    :return: pretul cartii
    '''
    return carte[3]


def getDiscountType(carte):
    '''
    Determina tipul de reducere al cartii
    :param carte: cartea
    :return: tipul de reducere al cartii
    '''
    return carte[4]


def toString(carte):
    '''
    Returneaza cartea intr-un anumit format
    :param carte: cartea
    :return: cartea intr-un anumit format
    '''
    return "Id: {}, Titlu: {}, Gen carte: {}, Pret: {}, Tip reducere: {}".format(
        getId(carte),
        getTitle(carte),
        getBookType(carte),
        getPrice(carte),
        getDiscountType(carte)
    )
