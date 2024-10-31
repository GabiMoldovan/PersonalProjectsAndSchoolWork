from UI.UserInterface import UIadaugaCarte, showBooks


def testUNDOREDO():
    lista = []

    # 1-4

    undoList = []
    redoList = []
    undoList.append(lista)
    redoList.clear()
    lista = lista + [UIadaugaCarte("1", "Dumbrava minunata", "Basm", 15, "none", lista)]
    undoList.append(lista)
    redoList.clear()
    lista = lista + [UIadaugaCarte("2", "Povestea lui Harap-Alb", "Basm", 1, "none", lista)]
    undoList.append(lista)
    redoList.clear()
    lista = lista + [UIadaugaCarte("3", "Moara cu noroc", "Nuvela", 20, "silver", lista)]

    # 5

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    # showBooks(lista)

    assert len(lista) == 2

    # 6

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    # showBooks(lista)

    assert len(lista) == 1

    # 7

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    # showBooks(lista)

    assert len(lista) == 0

    # 8

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    # showBooks(lista)

    assert len(lista) == 0

    # 9

    undoList.append(lista)
    redoList.clear()
    lista = lista + [UIadaugaCarte("1", "Dumbrava minunata", "Basm", 15, "none", lista)]
    undoList.append(lista)
    redoList.clear()
    lista = lista + [UIadaugaCarte("2", "Povestea lui Harap-Alb", "Basm", 1, "none", lista)]
    undoList.append(lista)
    redoList.clear()
    lista = lista + [UIadaugaCarte("3", "Moara cu noroc", "Nuvela", 20, "silver", lista)]

    # 10

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    assert len(lista) == 3

    # 11

    redoList.append(lista)
    lista = undoList.pop()
    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 1

    # 12

    undoList.append(lista)
    lista = redoList.pop()

    assert len(lista) == 2

    # 13
    undoList.append(lista)
    lista = redoList.pop()

    assert len(lista) == 3

    # 14

    redoList.append(lista)
    lista = undoList.pop()
    redoList.append(lista)
    lista = undoList.pop()

    assert len(lista) == 1

    # 15

    undoList.append(lista)
    redoList.clear()
    lista = lista + [UIadaugaCarte("5", "Ion", "Roman", 13, "none", lista)]
    assert len(lista) == 2

    # 16

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    assert len(lista) == 2

    # 17

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    assert len(lista) == 1

    # 18

    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()

    assert len(lista) == 0

    # 19

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    assert len(lista) == 2

    # 20

    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()

    assert len(lista) == 2
