import random
import string
from random import randint

from Domain.card import CardClient
from Domain.cardValidator import ValideazaCard
from Domain.deleteAllGenerated import DeleteAllGenerated
from Domain.deleteOperation import DeleteOperation
from Repository.repositoryJson import RepositoryJson
from Service.cardService import CardService
from Service.timeManager import seAflaInIntervalCalendaristic
from Service.undoRedoService import UndoRedoService
from mySortMethode import mySort
from utils import clear_file
from Domain.addOperation import AddOperation


def testUndoRedoCard():
    '''
    Testare Undo Redo Card
    :return: None
    '''
    filename = "testUndoRedoCard.json"
    clear_file(filename)
    cardRepository = RepositoryJson(filename)
    undoRedoService = UndoRedoService()
    cardService = CardService
    assert cardRepository.read() == []

    card = CardClient("1", "petrescu",
                      "Andrei",
                      "4354537653",
                      "11.11.1111",
                      "2.22.2222",
                      52)
    cardRepository.adauga(card)
    assert cardRepository.read("1") == card

    undoRedoService.addUndoOperation(AddOperation(cardRepository, card))
    undoRedoService.undo()

    assert cardRepository.read() == []

    undoRedoService.redo()

    assert cardService(cardRepository,
                       ValideazaCard(),
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

    cardRepository.sterge("2")
    undoRedoService.addUndoOperation(DeleteOperation(cardRepository, card2))
    assert cardRepository.read() == []

    undoRedoService.undo()
    assert cardRepository.read() == [card2]

    undoRedoService.redo()
    assert cardRepository.read() == []

    undoRedoService.undo()

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
    assert len(cardRepository.read()) == 2

    undoRedoService.undo()
    assert cardRepository.read() == [card2]

    undoRedoService.redo()
    assert cardRepository.read() == [card2, card]

    undoRedoService.undo()
    undoRedoService.undo()
    assert cardRepository.read() == [card2]

    undoRedoService.redo()

    pct = []
    for card in cardRepository.read():
        pct.append(card.puncte)
    sortedPct = mySort(pct, reverse=True)

    assert sortedPct == [52, 45]

    clear_file(filename)

    listaCarduriNoi = []
    n = 10
    while n > 0:
        idCard = randint(1, 99999)
        nume = ''.join((random.choice(
            string.ascii_lowercase) for x in range(5)))
        prenume = ''.join((random.choice(
            string.ascii_lowercase) for x in range(5)))
        CNP = randint(100000000, 999999999)
        dataNasterii = str(
            randint(10, 30)) + "." + str(
            randint(10, 12)) + "." + str(
            randint(1980, 2020))
        dataInregistrarii = str(
            randint(1, 9)) + "." + str(
            randint(10, 12)) + "." + str(
            randint(2000, 2020))
        puncte = randint(0, 10)
        cardNou = CardClient(
            str(idCard), nume, prenume, CNP,
            dataNasterii, dataInregistrarii, puncte)
        cardRepository.adauga(cardNou)
        listaCarduriNoi.append(cardNou)
        n = n - 1
    undoRedoService.addUndoOperation(
        DeleteAllGenerated(cardRepository, listaCarduriNoi))

    # for card in cardRepository.read():
    #     print(card)

    assert len(cardRepository.read()) == 10

    undoRedoService.undo()
    assert len(cardRepository.read()) == 0

    undoRedoService.redo()
    assert len(cardRepository.read()) == 10

    undoRedoService.undo()
    assert len(cardRepository.read()) == 0
