from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.film import Film
from Domain.filmValidator import ValideazaFilm
from Domain.modifyOperation import ModifyOperation
from Repository.repositoryJson import RepositoryJson
from Service.filmService import FilmService
from Service.undoRedoService import UndoRedoService
from utils import clear_file


def testUndoRedoFilm():
    '''
    Testare Film
    :return: None
    '''
    filename = "testUndoRedoFilm.json"
    clear_file(filename)

    filmRepository = RepositoryJson(filename)
    assert filmRepository.read() == []

    undoRedoService = UndoRedoService()

    film = Film("1", "Viata la facultate", 2021, 9999999, True)
    filmRepository.adauga(film)
    assert filmRepository.read("1") == film

    undoRedoService.addUndoOperation(AddOperation(filmRepository, film))

    undoRedoService.undo()
    assert filmRepository.read() == []

    undoRedoService.redo()
    assert filmRepository.read("1") == film

    undoRedoService.redo()
    assert filmRepository.read("1") == film

    undoRedoService.redo()
    assert filmRepository.read("1") == film

    undoRedoService.undo()
    assert filmRepository.read() == []

    undoRedoService.redo()
    assert filmRepository.read("1") == film

    filmService = FilmService
    assert filmService(filmRepository,
                       ValideazaFilm(), undoRedoService).fullTextSearchInFilme(
        "a") == [[film]]
    assert filmService(filmRepository,
                       ValideazaFilm(), undoRedoService).fullTextSearchInFilme(
        "Viata") == [[film]]

    filmMod = Film("1", "test", 1352, 53, True)
    filmService(filmRepository, ValideazaFilm(), undoRedoService
                ).modifica("1", "test", 1352, 53, True)
    assert filmRepository.read("1") == filmMod

    undoRedoService.addUndoOperation(ModifyOperation(filmRepository, film,
                                                     filmMod))

    undoRedoService.undo()
    assert filmRepository.read() == [film]

    undoRedoService.redo()
    assert filmRepository.read() == [filmMod]

    undoRedoService.undo()
    assert filmRepository.read() == [film]

    undoRedoService.undo()
    assert filmRepository.read() == [film]

    undoRedoService.redo()
    assert filmRepository.read() == [filmMod]

    undoRedoService.redo()
    assert filmRepository.read() == [filmMod]

    filmRepository.sterge("1")
    assert filmRepository.read() == []

    undoRedoService.addUndoOperation(DeleteOperation(filmRepository, filmMod))

    undoRedoService.undo()
    assert filmRepository.read() == [filmMod]

    undoRedoService.redo()
    assert filmRepository.read() == []

    undoRedoService.undo()
    assert filmRepository.read() == [filmMod]

    undoRedoService.redo()
    assert filmRepository.read() == []

    undoRedoService.redo()
    assert filmRepository.read() == []

    undoRedoService.undo()
    assert filmRepository.read() == [filmMod]
