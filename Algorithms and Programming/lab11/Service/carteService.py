from Domain.carte import Carte
from Domain.carteValidator import CarteValidator
from Repository.json_repository import JsonRepository


class CarteService:
    def __init__(self, carteRepository: JsonRepository,
                 carteValidator: CarteValidator):
        self.carteRepository = carteRepository
        self.carteValidator = carteValidator

    def adauga(self, idCarte, titlu: str, categorie: str, nrpg: int, pret: int,
               autori: list):
        '''
        Metoda de adaugare a unei carti
        :param titlu: titlul cartii
        :param categorie: categoria cartii
        :param nrpg: nr de pagini
        :param pret: pretul cartii
        :param autori: lista cu id-urile autorilor
        :return: None
        '''
        carte = Carte(idCarte, titlu, categorie, nrpg, pret, autori)
        self.carteValidator.valideaza(carte)
        self.carteRepository.create(carte)

    def getAll(self):
        '''
        Functia care returneaza toate cartile din repository
        :return: cartile din repository
        '''
        return self.carteRepository.read()
