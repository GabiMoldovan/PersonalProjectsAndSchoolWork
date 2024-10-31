from Domain.entitate import Entitate
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class IncrementOperation(UndoRedoOperation):
    def __init__(self, repository: Repository,
                 obiectVechi: list[Entitate],
                 obiectNou: list[Entitate]):
        self.__repository = repository
        self.__obiectVechi = obiectVechi
        self.__obiectNou = obiectNou

    def doUndo(self):
        for obj in self.__obiectNou:
            self.__repository.sterge(str(obj.idEntitate))
        for obj in self.__obiectVechi:
            self.__repository.adauga(obj)

    def doRedo(self):
        for obj in self.__obiectVechi:
            self.__repository.sterge(str(obj.idEntitate))
        for obj in self.__obiectNou:
            self.__repository.adauga(obj)
