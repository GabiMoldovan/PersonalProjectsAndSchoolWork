from Domain.undoRedoOperation import UndoRedoOperation
from Repository.repository import Repository


class CascadeDeleteOperation(UndoRedoOperation):
    def __init__(self, repositoryUnu: Repository, repositoryDoi: Repository,
                 obiectStersUnu, obiectStersDoi):
        self.repositoryUnu = repositoryUnu
        self.repositoryDoi = repositoryDoi
        self.obiectStersUnu = obiectStersUnu
        self.obiectStersDoi = obiectStersDoi

    def doUndo(self):
        for entitate in self.obiectStersUnu:
            self.repositoryUnu.adauga(entitate)

        for entitate in self.obiectStersDoi:
            self.repositoryDoi.adauga(entitate)

    def doRedo(self):
        for entitate in self.obiectStersUnu:
            self.repositoryUnu.sterge(entitate.idEntitate)

        for entitate in self.obiectStersDoi:
            self.repositoryDoi.sterge(entitate.idEntitate)
