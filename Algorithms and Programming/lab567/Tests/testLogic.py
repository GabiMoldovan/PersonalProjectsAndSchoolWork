from CRUD.CRUD import adaugaCarte
from UI.UserInterface import UIadaugaCarte
from functions.Logic import checkIfTitleExists, isInTypeList, getAllTypes, getMinPriceofType, isInPriceList, \
    getAllPrices, countedTitle, deleteBookbyId, changeBookData, applyDiscounts, modifyTypeByTitle, \
    getTitlesWithMinPriceOfType, sortByPrice, getDistinctTitlesbyType


def testAllLogicFunctions():
    lista = []
    lista = adaugaCarte("1", "Dumbrava minunata", "Basm", 15, "none", lista)
    lista = adaugaCarte("2", "Povestea lui Harap-Alb", "Basm", 1, "none", lista)
    lista = adaugaCarte("3", "Moara cu noroc", "Nuvela", 10, "silver", lista)

    assert UIadaugaCarte("4", "Mara", "Nuvela", 20, "silver", lista) == ("4", "Mara", "Nuvela", 20, "silver")

    assert deleteBookbyId(lista, "3") == [
        ("1", "Dumbrava minunata", "Basm", 15, "none"), ("2", "Povestea lui Harap-Alb", "Basm", 1, "none")
    ]

    assert changeBookData(lista, "2", "Ion", "Roman", 5, "gold") == [
        ("1", "Dumbrava minunata", "Basm", 15, "none"),
        ("2", "Ion", "Roman", 5, "gold"),
        ("3", "Moara cu noroc", "Nuvela", 10, "silver")
    ]

    assert applyDiscounts(lista, "ambele") == [
        ("1", "Dumbrava minunata", "Basm", 15, "none"),
        ("2", "Povestea lui Harap-Alb", "Basm", 1, "none"),
        ("3", "Moara cu noroc", "Nuvela", 9.5, "silver")
    ]

    assert checkIfTitleExists(lista, "Povestea lui Harap-Alb") is True

    assert modifyTypeByTitle(lista, "Moara cu noroc", "Roman") == [
        ("1", "Dumbrava minunata", "Basm", 15, "none"),
        ("2", "Povestea lui Harap-Alb", "Basm", 1, "none"),
        ("3", "Moara cu noroc", "Roman", 10, "silver")
    ]

    assert isInTypeList(["Balada", "Roman", "Basm", "Comedie"], "Basm") is True
    assert getAllTypes(lista) == ["Basm", "Nuvela"]
    assert getMinPriceofType(lista, "Basm") == 1
    assert getTitlesWithMinPriceOfType("Basm", 1, lista) == ["Povestea lui Harap-Alb"]
    assert isInPriceList(["15", "34", "64", "24", "54"], "24") is True
    assert isInPriceList(["15", "34", "64", "24", "54"], "25") is False
    assert getAllPrices(lista) == [15, 1, 10]

    assert sortByPrice(lista) == [
        ("2", "Povestea lui Harap-Alb", "Basm", 1, "none"),
        ("3", "Moara cu noroc", "Nuvela", 10, "silver"),
        ("1", "Dumbrava minunata", "Basm", 15, "none")
    ]

    assert countedTitle(lista, "Ion") is False
    assert getDistinctTitlesbyType(lista, "Basm") == ["Dumbrava minunata", "Povestea lui Harap-Alb"]
