from CRUD.CRUD import adaugaCarte, checkValidIdtoAdd, checkifBookExists, checkValidDiscountType
from Domain.book import getId, getTitle, getBookType, getPrice, getDiscountType, createBook


def testCrud():
    lista = []
    book = createBook("1", "Dumbrava minunata", "Basm", 15, "none")
    lista = lista + [book]

    assert adaugaCarte("2", "Povestea lui Harap-Alb", "Basm", 1, "none", lista) == [
        ("1", "Dumbrava minunata", "Basm", 15, "none"),  ("2", "Povestea lui Harap-Alb", "Basm", 1, "none")
    ]
    assert len(lista) == 1
    assert getId(book) == "1"
    assert getTitle(book) == "Dumbrava minunata"
    assert getBookType(book) == "Basm"
    assert getPrice(book) == 15
    assert getDiscountType(book) == "none"
    assert checkValidIdtoAdd("1", lista) is False
    assert checkValidIdtoAdd("2", lista) is True
    assert checkifBookExists("1", lista) is True
    assert checkifBookExists("2", lista) is False
    assert checkValidDiscountType("none") is True
    assert checkValidDiscountType("test") is False
    assert checkValidDiscountType("gold") is True
