from Domain.carte import Carte
from Domain.carteValidator import CarteValidator
from Repository.json_repository import JsonRepository
from Service.carteService import CarteService
from utils import clear_file


def testing():
    '''
    Testare Card
    :return: None
    '''

    filename = "testcarte.json"
    clear_file(filename)
    carteRepository = JsonRepository(filename)

    carteValidator = CarteValidator()

    carteService = CarteService(carteRepository, carteValidator)

    assert carteRepository.read() == []
    carte = Carte(1, "test", "test", 5, 3, ["1"])

    carteRepository.create(carte)
    assert carteRepository.read() == [carte]
