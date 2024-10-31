from Domain.autor import Autor
from Domain.autorValidator import AutorValidator
from Repository.json_repository import JsonRepository


class AutorService:
    def __init__(self, autorRepository: JsonRepository,
                 autorValidator: AutorValidator):
        self.autorRepository = autorRepository
        self.autorValidator = autorValidator

    def adauga(self, id, nume: str, prenume: str, email: str):
        '''
        Metoda de adaugare a unui autor
        :param id: id-ul autorului
        :param nume: numele autorului
        :param prenume: prenumele autorului
        :param email: emailul autorului
        :return: None
        '''
        autor = Autor(id, nume, prenume, email)
        self.autorValidator.valideaza(autor)
        self.autorRepository.create(autor)

    def getAll(self):
        '''
        Functia care returneaza toti autorii din repository
        :return: toti autorii din repository
        '''
        return self.autorRepository.read()
