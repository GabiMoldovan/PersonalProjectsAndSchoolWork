from Domain.entitate import Entitate
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class DeleteOperation(UndoRedoOperation):
    def __init__(self, repository: Repository, obiectSters: Entitate):
        self.__repository = repository
        self.__obiectSters = obiectSters

    def doUndo(self):
        obj = self.__obiectSters
        self.__repository.adauga(obj)

    def doRedo(self):
        self.__repository.sterge(self.__obiectSters.idEntitate)
