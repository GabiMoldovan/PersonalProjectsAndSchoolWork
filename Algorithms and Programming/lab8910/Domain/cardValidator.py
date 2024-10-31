from Domain.card import CardClient
from Domain.cardError import CardError


class ValideazaCard:
    '''
    Clasa care valideaza Cardul
    '''
    def valideazaCardul(self, card: CardClient) -> None:
        '''
        Verifica daca cardul are un format ok
        :param card: Cardul
        :return: erorile specifice probleme daca exista, altfel None
        '''
        erori = []
        if isinstance(card.nume, str) is False:
            erori.append("Numele detinatorului "
                         "cardului nu este un sir de caractere sau este gol")
        if isinstance(card.prenume, str) is False:
            erori.append("Prenumele detinatorului "
                         "cardului nu este un sir de caractere sau este gol")
        dataNastere = card.dataNasterii
        if dataNastere[2] != "." or \
                dataNastere[5] != "." or len(dataNastere) > 10:
            erori.append("Formatul pentru "
                         "data nasterii este incorect ( dd.mm.yyyy )")
        dataInregistrare = card.dataInregistrarii
        if dataInregistrare[1] != "." or \
                dataInregistrare[4] != "." or len(dataInregistrare) > 9:
            erori.append("Formatul pentru "
                         "data inregistrarii este incorect ( d.mm.yyyy )")

        if card.CNP == "":
            erori.append("CNP-ul trebuie completat!")

        if len(erori) > 0:
            raise CardError(erori)
