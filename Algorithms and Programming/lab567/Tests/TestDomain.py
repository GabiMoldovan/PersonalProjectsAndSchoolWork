from Domain.book import createBook, getId, getTitle, getBookType, getPrice, getDiscountType


def testCarte():
    book = createBook("1", "Dumbrava minunata", "Basm", 15, "none")

    assert getId(book) == "1"
    assert getTitle(book) == "Dumbrava minunata"
    assert getBookType(book) == "Basm"
    assert getPrice(book) == 15
    assert getDiscountType(book) == "none"
