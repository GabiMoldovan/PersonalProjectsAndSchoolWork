from Domain import filmValidator
from Domain.film import Film
from Domain.filmValidator import ValideazaFilm
from Repository.repositoryJson import RepositoryJson
from Service.filmService import FilmService
from Service.undoRedoService import UndoRedoService
from utils import clear_file


def testFilm():
    '''
    Testare Film
    :return: None
    '''
    filename = "testfilm.json"
    clear_file(filename)

    filmRepository = RepositoryJson(filename)
    assert filmRepository.read() == []

    film = Film("1", "Viata la facultate", 2021, 9999999, True)
    filmRepository.adauga(film)
    assert filmRepository.read("1") == film

    filmService = FilmService
    assert filmService(filmRepository,
                       filmValidator, UndoRedoService()).fullTextSearchInFilme(
        "a") == [[film]]
    assert filmService(filmRepository,
                       filmValidator, UndoRedoService()).fullTextSearchInFilme(
        "Viata") == [[film]]

    filmMod = Film("1", "test", 1352, 53, True)
    filmService(filmRepository, ValideazaFilm(), UndoRedoService()
                ).modifica("1", "test", 1352, 53, True)
    assert filmRepository.read("1") == filmMod

    filmRepository.sterge("1")
    assert filmRepository.read() == []
