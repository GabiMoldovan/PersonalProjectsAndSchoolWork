from Domain.entitate import Entitate
from Repository.repository import Repository


class RepositoryInMemory(Repository):
    def __init__(self):
        self.entitati = {}

    def read(self, idEntitate=None):
        '''
        Citeste entitatea cu idEntitate din fisiere
        :param idEntitate: id-ul entitatii
        :return: entitatea
        '''
        if idEntitate is None:
            return list(self.entitati.values())

        if idEntitate in self.entitati:
            return self.entitati[idEntitate]
        else:
            return None

    def adauga(self, entitate: Entitate) -> None:
        '''
        Adauga entitatea in fisier
        :param entitate: entitatea
        :return: None
        '''
        if self.read(entitate.idEntitate) is not None:
            raise KeyError("Exista deja o entitate cu id-ul dat!")
        self.entitati[entitate.idEntitate] = entitate

    def sterge(self, idEntitate: str) -> None:
        '''
        Sterge entitatea din fisier
        :param idEntitate: id-ul entitatii
        :return: None
        '''
        if self.read(idEntitate) is None:
            raise KeyError("Nu exista nicio entitate cu id-ul dat!")
        del self.entitati[idEntitate]

    def modifica(self, entitate: Entitate) -> None:
        '''
        Modifica parametri entitatii
        :param entitate: entitatea
        :return: None
        '''
        self.entitati[entitate.idEntitate] = entitate
