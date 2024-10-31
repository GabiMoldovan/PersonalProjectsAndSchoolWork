from Domain.addOperation import AddOperation
from Domain.deleteAllOperation import DeleteAllOperation
from Domain.deleteOperation import DeleteOperation
from Domain.modifyOperation import ModifyOperation
from Domain.rezervare import Rezervare
from Domain.rezervareValidator import ValideazaRezervare
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService
from mySortMethode import mySort


class RezervareService:
    '''
    Clasa pentru comenzile Rezervarii
    '''
    def __init__(self,
                 rezervareRepository: Repository,
                 cardRepository: Repository,
                 filmRepository: Repository,
                 rezervareValidator: ValideazaRezervare,
                 undoRedoService: UndoRedoService) -> None:
        self.__rezervareRepository = rezervareRepository
        self.__cardRepository = cardRepository
        self.__filmRepository = filmRepository
        self.__rezervareValidator = rezervareValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        '''
        returneaza toate rezervarile
        :return: toate rezervarile
        '''
        return self.__rezervareRepository.read()

    def adauga(self,
               idRezervare,
               idFilm,
               idCardClient,
               data,
               ora) -> None:
        '''
        Adauga o rezervare in repository
        :param idRezervare: id
        :param idFilm: id
        :param idCardClient: id
        :param data: data
        :param ora: ora
        :return: None
        '''
        if self.__cardRepository.read(idCardClient) is None:
            raise KeyError("Nu exista niciun card cu id-ul dat!")
        if self.__filmRepository.read(idFilm) is None:
            raise KeyError("Nu exista niciun film cu id-ul dat!")

        rezervare = Rezervare(
            idRezervare,
            idFilm,
            idCardClient,
            data,
            ora)
        self.__rezervareValidator.valideazaRezervarea(rezervare)
        self.__rezervareRepository.adauga(rezervare)
        self.__undoRedoService.addUndoOperation(
            AddOperation(self.__rezervareRepository, rezervare))

    def sterge(self, idRezervare) -> None:
        '''
        Sterge o rezervare din repository
        :param idRezervare: id-ul rezervarii
        :return: None
        '''
        for rezervare in self.__rezervareRepository.read():
            if rezervare.idEntitate == idRezervare:
                self.__undoRedoService.addUndoOperation(DeleteOperation(
                    self.__rezervareRepository, rezervare))
                break
        self.__rezervareRepository.sterge(idRezervare)

    def modifica(self,
                 idRezervare,
                 idFilm,
                 idCardClient,
                 data,
                 ora) -> None:
        '''
        Modifica parametrii unei rezervari
        :param idRezervare: id-ul rezevarii
        :param idFilm: noul id film
        :param idCardClient: noul id card
        :param data: noua data
        :param ora: noua ora
        :return: None
        '''
        if self.__cardRepository.read(idCardClient) is None:
            raise KeyError("Nu exista niciun card cu id-ul dat!")
        if self.__filmRepository.read(idFilm) is None:
            raise KeyError("Nu exista niciun film cu id-ul dat!")

        rezervareVeche = self.__rezervareRepository.read(idRezervare)
        rezervare = Rezervare(
            idRezervare,
            idFilm,
            idCardClient,
            data,
            ora)
        self.__rezervareValidator.valideazaRezervarea(rezervare)
        self.__rezervareRepository.modifica(rezervare)
        self.__undoRedoService.addUndoOperation(ModifyOperation(
            self.__rezervareRepository, rezervareVeche, rezervare)
        )

    def ordoneazaFilmeDupaRezervari(self) -> list:
        '''
        Returneaza lista de filme in ordine
        descrescatoare dupa numarul de rezervari
        :return: lista de filme in ordine
        descrescatoare dupa numarul de rezervari
        '''
        filme = []
        nrRezervari = {}
        for film in self.__filmRepository.read():
            filme.append(film.idEntitate)
        for film in filme:
            nrRezervari[film] = int(0)
        for rezervare in self.__rezervareRepository.read():
            nrRezervari[rezervare.idFilm] += int(1)
        return mySort(filme, key=lambda x: -int(x))

    def stergeRezervariIntervalZile(self, ziUnu, ziDoi, lenRezervari,
                                    listaRezervari) -> None:
        '''
        Sterge toate rezervarile care se afla intr-un interval calendaristic
        :param ziUnu: primul capat al intervalului
        :param ziDoi: al doilea capat al intervalului
        :return: None
        '''
        ind = int(0)
        if int(lenRezervari) > int(0):
            for rezervare in self.__rezervareRepository.read():
                ind += int(1)
                if ind == lenRezervari:
                    ziRezervare = rezervare.data
                    idulRezervarii = rezervare.idEntitate
                    ziRezervare = ziRezervare[0] + ziRezervare[1]
                    if ziUnu >= ziRezervare and ziRezervare <= ziDoi:
                        listaRezervari.append(Rezervare(rezervare.idEntitate,
                                                        rezervare.idFilm,
                                                        rezervare.idCardClient,
                                                        rezervare.data,
                                                        rezervare.ora)
                                              )
                        self.__rezervareRepository.sterge(idulRezervarii)
                    return self.stergeRezervariIntervalZile(ziUnu,
                                                            ziDoi,
                                                            int(lenRezervari) -
                                                            int(1),
                                                            listaRezervari)
                break
        if int(lenRezervari) == int(0):
            self.__undoRedoService.addUndoOperation(DeleteAllOperation(
                self.__rezervareRepository,
                listaRezervari))

    def stergeCards(self, idCard, rezervariSterse) -> None:
        '''
        Functie care sterge rezervarile care au idCard
        :param idCard: id-ul cardului
        :return: None
        '''
        for rezervare in self.getAll():
            if rezervare.idCardClient == idCard:
                rezervariSterse.append(rezervare)
                self.sterge(rezervare.idEntitate)
