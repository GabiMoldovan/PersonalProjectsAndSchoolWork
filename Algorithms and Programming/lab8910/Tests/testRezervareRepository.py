from Domain.rezervare import Rezervare
from Repository.repositoryJson import RepositoryJson
from Service.rezervareService import RezervareService
from utils import clear_file


def testRezervare():
    '''
    Testare
    :return: Rezervare
    '''
    filename = "testrezervare.json"
    clear_file(filename)

    rezervaredRepository = RepositoryJson(filename)
    rezervareService = RezervareService
    assert rezervaredRepository.read() == []

    rezervare = Rezervare("1", 1, 1, "21.05.2021", "16:00")
    rezervaredRepository.adauga(rezervare)
    assert rezervaredRepository.read("1") == rezervare

    rezervaredRepository.sterge("1")
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
