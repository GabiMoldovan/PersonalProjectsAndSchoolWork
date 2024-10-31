from Domain import cardValidator
from Domain.card import CardClient
from Repository.repositoryJson import RepositoryJson
from Service.cardService import CardService
from Service.timeManager import seAflaInIntervalCalendaristic
from Service.undoRedoService import UndoRedoService
from mySortMethode import mySort
from utils import clear_file


def testCard():
    '''
    Testare Card
    :return: None
    '''
    filename = "testcard.json"
    clear_file(filename)
    cardRepository = RepositoryJson(filename)
    assert cardRepository.read() == []

    card = CardClient("1", "petrescu",
                      "Andrei",
                      "4354537653",
                      "11.11.1111",
                      "2.22.2222",
                      52)
    cardRepository.adauga(card)
    assert cardRepository.read("1") == card

    cardService = CardService
    assert cardService(cardRepository,
                       cardValidator,
                       UndoRedoService()).fullTextSearchInCard("escu") \
           == [[card]]

    cardRepository.sterge("1")
    assert cardRepository.read() == []

    card2 = CardClient("2", "test",
                       "testtest",
                       "757357357",
                       "22.22.2222",
                       "4.44.4444",
                       45)
    cardRepository.adauga(card2)

    rezultat = []
    dataUnu = "10.11.1111"
    dataDoi = "13.11.1111"
    for card in cardRepository.read():
        if seAflaInIntervalCalendaristic(dataUnu,
                                         dataDoi,
                                         card.dataNasterii
                                         ) is True:
            rezultat.append(card.idCard)

    assert rezultat == []

    card = CardClient("1", "petrescu",
                      "Andrei",
                      "4354537653",
                      "11.11.1111",
                      "2.22.2222",
                      52)
    cardRepository.adauga(card)

    pct = []
    for card in cardRepository.read():
        pct.append(card.puncte)
    sortedPct = mySort(pct, reverse=True)

    assert sortedPct == [52, 45]
