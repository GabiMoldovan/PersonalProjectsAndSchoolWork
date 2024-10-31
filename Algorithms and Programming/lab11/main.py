from Domain.autorValidator import AutorValidator
from Domain.carteValidator import CarteValidator
from Repository.json_repository import JsonRepository

# teste
# PEP8 !!!
# specificatii
# ID
from Service.autorService import AutorService
from Service.carteService import CarteService
from Teste.teste import testing
from UserInterface.UI import Console


def main():
    '''
    Main-ul programului care paseaza parametrii catre consola si o apeleaza
    :return: None
    '''
    carteRepository = JsonRepository("carti.json")
    autorRepository = JsonRepository("autori.json")
    carteValidator = CarteValidator()
    autorValidator = AutorValidator()

    carteService = CarteService(carteRepository,
                                carteValidator)
    autorService = AutorService(autorRepository,
                                autorValidator)

    console = Console(carteService, autorService)
    console.runMenu()


if __name__ == '__main__':
    testing()
    main()
