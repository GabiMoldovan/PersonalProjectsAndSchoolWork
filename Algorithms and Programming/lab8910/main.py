from Domain.cardValidator import ValideazaCard
from Domain.filmValidator import ValideazaFilm
from Domain.rezervareValidator import ValideazaRezervare
from Repository.repositoryJson import RepositoryJson
from Service.cardService import CardService
from Service.filmService import FilmService
from Service.rezervareService import RezervareService
from Service.undoRedoService import UndoRedoService
from Tests.testCardRepository import testCard
from Tests.testFilmRepository import testFilm
from Tests.testRezervareRepository import testRezervare
from Tests.testUndoRedoCard import testUndoRedoCard
from Tests.testUndoRedoFilm import testUndoRedoFilm
from Tests.testUndoRedoRezervare import testUndoRedoRezervare
from UI.consola import Consola


def main():
    '''
    Pasarea parametrilor catre functii si apelare consola
    :return: None
    '''
    undoRedoService = UndoRedoService()
    cardRepositoryJson = RepositoryJson("carduri.json")
    cardValidator = ValideazaCard()
    cardService = CardService(cardRepositoryJson, cardValidator,
                              undoRedoService)

    filmRepositoryJson = RepositoryJson("filme.json")
    filmValidator = ValideazaFilm()
    filmService = FilmService(filmRepositoryJson, filmValidator,
                              undoRedoService)

    rezervareRepositoryJson = RepositoryJson("rezervari.json")
    rezervareValidator = ValideazaRezervare()
    rezervareService = RezervareService(
        rezervareRepositoryJson,
        cardRepositoryJson,
        filmRepositoryJson,
        rezervareValidator,
        undoRedoService
    )

    testCard()
    testFilm()
    testRezervare()
    testUndoRedoCard()
    testUndoRedoFilm()
    testUndoRedoRezervare()
    consola = Consola(cardService, filmService, cardRepositoryJson,
                      rezervareService, undoRedoService,
                      rezervareRepositoryJson)

    consola.runMenu()


if __name__ == "__main__":
    main()
    exit(0)
