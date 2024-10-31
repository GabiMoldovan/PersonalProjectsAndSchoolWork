from Domain.entitate import Entitate
from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class DeleteAllGenerated(UndoRedoOperation):
    def __init__(self, repository: Repository, obiecteSters: list[Entitate]):
        self.__repository = repository
        self.__obiecteSters = obiecteSters

    def doRedo(self):
        for obj in self.__obiecteSters:
            self.__repository.adauga(obj)

    def doUndo(self):
        for obj in self.__obiecteSters:
            self.__repository.sterge(str(obj.idEntitate))
