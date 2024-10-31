from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.film import Film
from Domain.filmValidator import ValideazaFilm
from Domain.modifyOperation import ModifyOperation
from Repository.repository import Repository
from Service.undoRedoService import UndoRedoService


class FilmService:
    '''
    Clasa pentru comenzile Filmului
    '''
    def __init__(self,
                 filmRepository: Repository,
                 filmValidator: ValideazaFilm,
                 undoRedoService: UndoRedoService):
        self.__filmRepository = filmRepository
        self.__filmValidator = filmValidator
        self.__undoRedoService = undoRedoService

    def getAll(self):
        '''
        returneaza toate cardurile din fisierul json
        :return: toate cardurile din fisierul json
        '''
        return self.__filmRepository.read()

    def adauga(self, idFilm, titlu, anAparitie, pretBilet, inProgram) -> None:
        '''
        Creeaza si adauga un film in repository
        :param idFilm: id-ul
        :param titlu: titlul
        :param anAparitie: anul aparitiei
        :param pretBilet: pret bilet
        :param inProgram: in program
        :return: None
        '''
        film = Film(
            idFilm,
            titlu,
            anAparitie,
            pretBilet,
            inProgram)
        self.__filmValidator.valideazaFilmul(film)
        self.__filmRepository.adauga(film)
        self.__undoRedoService.addUndoOperation(
            AddOperation(self.__filmRepository, film))

    def sterge(self, idFilm) -> None:
        '''
        Sterge din repository un film cu id-ul dat
        :param idFilm: id-ul dat
        :return: None
        '''
        for film in self.__filmRepository.read():
            if film.idEntitate == idFilm:
                self.__undoRedoService.addUndoOperation(DeleteOperation(
                    self.__filmRepository, film))
                break
        self.__filmRepository.sterge(idFilm)

    def modifica(self,
                 idFilm,
                 titlu,
                 anAparitie,
                 pretBilet,
                 inProgram) -> None:
        '''
        Modifica toti parametrii unui film
        :param idFilm: id-ul nou
        :param titlu: titlul nou
        :param anAparitie: anul aparitiei nou
        :param pretBilet: pretul nou
        :param inProgram: noul status
        :return: None
        '''
        filmVechi = self.__filmRepository.read(idFilm)
        film = Film(
            idFilm,
            titlu,
            anAparitie,
            pretBilet,
            inProgram)
        self.__filmValidator.valideazaFilmul(film)
        self.__filmRepository.modifica(film)
        self.__undoRedoService.addUndoOperation(ModifyOperation(
            self.__filmRepository, filmVechi, film)
        )

    def fullTextSearchInFilme(self, text) -> list:
        '''
        Cauta textul in fiecare camp string al entitatii
        :param text: textul cautat
        :return: None
        '''
        rezultat = []
        # for film in self.getAll():
        #     if film.titlu.find(text) > -1 or str(film.idEntitate).find(text):
        #         rezultat.append(film)
        rezultat.append(list(filter(lambda x: x.titlu.find(text) > -1 or
                                    str(x.idEntitate).find(text),
                                    self.getAll())))
        return list(rezultat)
