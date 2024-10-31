from Domain.addOperation import AddOperation
from Domain.card import CardClient
from Domain.cardValidator import ValideazaCard
from Domain.deleteOperation import DeleteOperation
from Domain.modifyOperation import ModifyOperation
from Repository.repository import Repository
from Service.timeManager import seAflaInIntervalCalendaristic
from Service.undoRedoService import UndoRedoService


class CardService:
    '''
    Clasa pentru comenzile cardului
    '''
    def __init__(self,
                 cardRepository: Repository,
                 cardValidator: ValideazaCard,
                 undoRedoService: UndoRedoService):
        self.__cardRepository = cardRepository
        self.__cardValidator = cardValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        '''
        returneaza toate cardurile din repository
        :return: toate cardurile din repository
        '''
        return self.__cardRepository.read()

    def adauga(self, idCard, nume, prenume,
               CNP, dataNasterii,
               dataInregistrarii, puncte) -> None:
        '''
        Creeaza cardul si il adauga la repository
        :param idCard: id-ul
        :param nume: numele
        :param prenume: prenumele
        :param CNP: CNP-ul
        :param dataNasterii: data nasterii
        :param dataInregistrarii: data inregistrarii
        :param puncte: nr puncte
        :return: None
        '''
        cardadd = CardClient(idCard,
                             nume,
                             prenume,
                             CNP,
                             dataNasterii,
                             dataInregistrarii,
                             puncte)
        self.__cardValidator.valideazaCardul(cardadd)
        self.__cardRepository.adauga(cardadd)
        self.__undoRedoService.addUndoOperation(
            AddOperation(self.__cardRepository, cardadd))

    def sterge(self, idCard) -> None:
        '''
        sterge cardul din repository cu id-ul dat
        :param idCard: id-ul dat
        :return: None
        '''
        for card in self.__cardRepository.read():
            if card.idEntitate == idCard or int(card.idEntitate) == \
                    int(idCard):
                self.__undoRedoService.addUndoOperation(DeleteOperation(
                    self.__cardRepository, card))
                break
        self.__cardRepository.sterge(idCard)

    def modifica(self, idCard, nume, prenume,
                 CNP, dataNasterii,
                 dataInregistrarii, puncte) -> None:
        '''
        Creeaza cardul cu parametrii modificati
        :param idCard: id-ul nou
        :param nume: numele nou
        :param prenume: prenumele nou
        :param CNP: CNP-ul nou
        :param dataNasterii: noua data a nasterii
        :param dataInregistrarii: noua data a inregistrarii
        :param puncte: nr nou de pct
        :return: None
        '''
        cardVechi = self.__cardRepository.read(idCard)
        card = CardClient(idCard, nume,
                          prenume, CNP, dataNasterii,
                          dataInregistrarii, puncte)
        self.__cardValidator.valideazaCardul(card)
        self.__cardRepository.modifica(card)
        self.__undoRedoService.addUndoOperation(ModifyOperation(
            self.__cardRepository, cardVechi, card)
        )

    def fullTextSearchInCard(self, text) -> list:
        '''
        Cauta text in parametrii string ai entitatii card
        :param text: textul cautat
        :return: cardurile in care apare textul cautat
        '''
        rezultat = []
        # for card in self.getAll():
        #     if card.nume.find(text) > -1 or card.prenume.find(text) > -1\
        #             or str(card.idEntitate).find(text) > -1:
        #         rezultat.append(card)
        rezultat.append(list(filter(lambda x: x.nume.find(text) > -1 or
                                    x.prenume.find(text) > -1 or
                                    str(x.idEntitate).find(text) >
                                    -1, self.getAll())))
        return rezultat

    def uiGetCarduriDescrDupaNrPct(self) -> list:
        '''
        Calculeaza lista de puncte ale cardurilor si o sorteaza descrescator
        :return: lista de puncte ale cardurilor sortata descrescator
        '''
        pct = []
        for card in self.__cardRepository.read():
            pct.append(card.puncte)
        return sorted(pct, key=lambda x: -int(x))

    def getBDayCardsFromInterval(self, dataUnu, dataDoi) -> list:
        '''
        Determina o lista de carduri al caror proprietari a
        re data nasterii intr-un interval calendaristic
        :param dataUnu: primul capat al intervalului
        :param dataDoi: al doilea capat al intervalului
        :return: cardurile al caror proprietari are
        data nasterii intr-un interval calendaristic
        '''
        dataUnuStr = str(dataUnu)
        dataDoiStr = str(dataDoi)
        dataUnuStr = dataUnuStr[6] + dataUnuStr[7] + "." + dataUnuStr[4] + \
            dataUnuStr[5] + "." + dataUnuStr[0] + dataUnuStr[1] + \
            dataUnuStr[2] + dataUnuStr[3]
        dataDoiStr = dataDoiStr[6] + dataDoiStr[7] + "." + dataDoiStr[4] + \
            dataDoiStr[5] + "." + dataDoiStr[0] + dataDoiStr[1] + \
            dataDoiStr[2] + dataDoiStr[3]
        rezultat = []
        for card in self.__cardRepository.read():
            if seAflaInIntervalCalendaristic(dataUnuStr,
                                             dataDoiStr,
                                             card.dataNasterii
                                             ) is True:
                rezultat.append(card.idEntitate)
        return rezultat

    def aplicaPuncte(self, idCardClient, idFilmm) -> None:
        '''
        Functie care aplica punctele dupa ce se face o rezervare
        :param idCardClient: id-ul cardului
        :param idFilmm: id-ul filmului
        :return: None
        '''
        for card in self.getAll():
            if card.idEntitate == idCardClient:
                for film in self.__filmService.getAll():
                    if film.idEntitate == idFilmm:
                        self.__cardService.modifica(
                            idCardClient, card.nume,
                            card.prenume,
                            card.CNP,
                            card.dataNasterii,
                            card.dataInregistrarii,
                            int(card.puncte)
                            +
                            int(film.pretBilet) // int(10))
