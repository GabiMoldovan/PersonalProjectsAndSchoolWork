from Domain.addOperation import AddOperation
from Domain.deleteOperation import DeleteOperation
from Domain.rezervare import Rezervare
from Repository.repositoryJson import RepositoryJson
from Service.rezervareService import RezervareService
from Service.undoRedoService import UndoRedoService
from utils import clear_file


def testUndoRedoRezervare():
    '''
    Testare
    :return: Rezervare
    '''
    filename = "testrezervare.json"
    clear_file(filename)

    undoRedoService = UndoRedoService()

    rezervaredRepository = RepositoryJson(filename)
    rezervareService = RezervareService
    assert rezervaredRepository.read() == []

    rezervare = Rezervare("1", 1, 1, "21.05.2021", "16:00")
    rezervaredRepository.adauga(rezervare)
    assert rezervaredRepository.read("1") == rezervare

    undoRedoService.addUndoOperation(AddOperation(rezervaredRepository,
                                                  rezervare))

    undoRedoService.undo()
    assert rezervaredRepository.read() == []

    undoRedoService.redo()
    assert rezervaredRepository.read() == [rezervare]

    undoRedoService.undo()
    assert rezervaredRepository.read() == []

    undoRedoService.redo()
    assert rezervaredRepository.read() == [rezervare]

    undoRedoService.redo()
    assert rezervaredRepository.read() == [rezervare]

    undoRedoService.redo()
    assert rezervaredRepository.read() == [rezervare]

    rezervaredRepository.sterge("1")
    assert rezervaredRepository.read() == []

    undoRedoService.addUndoOperation(DeleteOperation(rezervaredRepository,
                                                     rezervare))

    undoRedoService.undo()
    assert rezervaredRepository.read() == [rezervare]

    undoRedoService.redo()
    assert rezervaredRepository.read() == []

    undoRedoService.redo()
    assert rezervaredRepository.read() == []

    undoRedoService.redo()
    assert rezervaredRepository.read() == []

    ziUnu = "19"
    ziDoi = "22"

    for rezervare in rezervaredRepository.read():
        ziRezervare = rezervare.data
        idulRezervarii = rezervare.idEntitate
        ziRezervare = ziRezervare[0] + ziRezervare[1]
        if ziRezervare >= ziUnu and ziRezervare <= ziDoi:
            rezervaredRepository.sterge(idulRezervarii)

    assert rezervaredRepository.read() == []
