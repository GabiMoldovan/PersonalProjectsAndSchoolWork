from CRUD.CRUD import checkifBookExists, checkValidDiscountType, checkValidIdtoAdd
from Domain.book import createBook, getId, getTitle, getBookType, getPrice, getDiscountType
from functions.Logic import deleteBookbyId, changeBookData, applyDiscounts, modifyTypeByTitle, \
    sortByPrice, getAllTypes, getMinPriceofType, getTitlesWithMinPriceOfType, checkIfTitleExists, \
    getDistinctTitlesbyType


def showBooks(lista):
    '''
    Afiseaza toate cartile din lista
    :param lista: lista de carti
    :return: None
    '''
    for book in lista:
        print("Id: " + getId(book))
        print("Titlu: " + getTitle(book))
        print("Gen: " + getBookType(book))
        print("Pret: " + str(getPrice(book)))
        print("Tip reducere: " + getDiscountType(book))
        print()


def UIadaugaCarte(id, titlu, gen, pret, tipReducere, lista):
    '''
    Creeaza o carte
    :return: cartea creata
    '''
    while checkValidIdtoAdd(id, lista) is False or id == "":
        id = input("Exista deja o carte cu acest ID sau campul este gol! dati alt ID: ")
    while titlu == "":
        titlu = input("Campul titlu nu poate fi lasat gol, dati un titlu: ")
    while gen == "":
        gen = input("Campul gen nu poate fi lasat gol, dati un titlu: ")
    while checkValidDiscountType(tipReducere) is False:
        tipReducere = input("Dati un tip de reducere valid(none/silver/gold): ")
    return createBook(id, titlu, gen, pret, tipReducere)


def printMenu():
    '''
    Afiseaza meniul de optiuni
    :return: None
    '''
    print("Optiunile sunt:")
    print("0. Afiseaza cartile din librarie")
    print("1. Adauga o carte in librarie")
    print("2. Sterge o carte din librarie")
    print("3. Modifica datele unei carti din librarie")
    print("4. Aplica o reducere de tip silver/gold sau pe ambele")
    print("5. Modifica genul pentru un titlu dat")
    print("6. Afiseaza pretul minim pentru fiecare gen")
    print("7. Ordoneaza vanzarile crescator dupa pret")
    print("8. Afisarea numarului de titluri distincte din fiecare gen")
    print("9. Undo")
    print("10. Redo")
    print("x. Termina programul")


def runMenu(lista):
    '''
    Functia care ruleaza meniul
    :param lista: lista de carti
    :return: None
    '''

    undoList = []
    redoList = []

    while True:
        printMenu()
        print()
        option = input("Scrie numarul aferent unei optiuni: ")

        if option == "0":
            print()
            print("Cartile din librarie sunt:")
            showBooks(lista)

        elif option == "1":
            id = input("Dati id: ")
            titlu = input("Dati titlu: ")
            gen = input("Dati gen: ")
            while True:
                try:
                    pret = int(input("Dati pret: "))
                    break
                except ValueError:
                    print("Nu ati dat un numar mai mare ca 0!")
            tipReducere = input("Dati tip reducere: ")
            undoList.append(lista)
            redoList.clear()
            lista = lista + [UIadaugaCarte(id, titlu, gen, pret, tipReducere, lista)]
            print("Cartea a fost adaugata cu succes!")

        elif option == "2":
            id = input("Dati id-ul cartii care doriti sa fie stearsa: ")
            while checkifBookExists(id, lista) is False:
                id = input("Dati un id valid: ")
            undoList.append(lista)
            redoList.clear()
            lista = deleteBookbyId(lista, id)
            print("Cartea a fost stearsa cu succes!")

        elif option == "3":
            id = input("Dati id: ")
            while checkifBookExists(id, lista) is False or id == "":
                id = input("Cartea cu id-ul dat nu exista sau nu este un numar, dati un id valid: ")
            titlu = input("Dati titlu: ")
            while titlu == "":
                titlu = input("Titlul nu trebuie sa fie gol! dati unul: ")
            gen = input("Dati genul: ")
            while gen == "":
                gen = input("Genul nu trebuie sa fie gol! dati unul: ")
            while True:
                try:
                    pret = int(input("Dati pretul: "))
                    break
                except ValueError:
                    print("Nu ati dat un numar natural pentru pret!")
            tipReducere = input("Dati tipul reducerii (none/silver/gold): ")
            while checkValidDiscountType(tipReducere) is False:
                tipReducere = input("Dati un tip de reducere valid (none/silver/gold):")
            undoList.append(lista)
            redoList.clear()
            lista = changeBookData(lista, id, titlu, gen, pret, tipReducere)
            print("Datele cartii au fost schimbate cu succes!")

        elif option == "4":
            discountType = input("Dati tipul de reducere(silver/gold/ambele): ")
            while discountType != "ambele" and discountType != "silver" and discountType != "gold":
                discountType = input("Dati un tip valid de reducere(silver/gold/ambele): ")
            undoList.append(lista)
            redoList.clear()
            lista = applyDiscounts(lista, discountType)
            print("Reducerea a fost aplicata cu succes!")

        elif option == "5":
            title = input("Dati titlul: ")
            while checkIfTitleExists(lista, title) is False:
                title = input("Dati un titlu care se afla in librarie: ")
            newType = input("Dati genul: ")
            while newType == "":
                newType = input("Campul gen trebuie completat: ")
            undoList.append(lista)
            redoList.clear()
            lista = modifyTypeByTitle(lista, title, newType)
            print("Modificarea genului cartii a fost aplicata cu succes!")

        elif option == "6":
            print()
            listaGenuri = []
            listaGenuri = getAllTypes(lista)
            for gen in listaGenuri:
                pretGen = getMinPriceofType(lista, gen)
                titluriPreturiMinimePtGen = getTitlesWithMinPriceOfType(gen, pretGen, lista)
                print("Cartea/Cartile cu pretul minim ( de " + str(pretGen) + " ) al genului " + gen +
                      " sunt:", end=" ")
                for titlu in titluriPreturiMinimePtGen:
                    if titlu is not titluriPreturiMinimePtGen[int(len(titluriPreturiMinimePtGen))-int(1)]:
                        print("\"" + titlu + "\"", end=", ")
                    else:
                        print("\"" + titlu + "\"", end=".")
                print()

        elif option == "7":
            undoList.append(lista)
            redoList.clear()
            lista = sortByPrice(lista)
            print("Ordonarea a avut loc cu succes!")

        elif option == "8":
            print()
            listaGenuri = []
            listaGenuri = getAllTypes(lista)
            print("Numarul de titluri distincte din fiecare gen sunt:")
            for gen in listaGenuri:
                listaTitluriDistincte = getDistinctTitlesbyType(lista, gen)
                print("Numarul de titluri distincte care au genul " + gen + " este: " + str(len(listaTitluriDistincte)))

        elif option == "9":
            if len(undoList) > 0:
                redoList.append(lista)
                lista = undoList.pop()
                print("Operatia Undo s-a executat cu succes!")
            else:
                print("Nu se poate executa undo!")

        elif option == "10":
            if len(redoList) > 0:
                undoList.append(lista)
                lista = redoList.pop()
                print("Operatia Redo s-a executat cu succes!")
            else:
                print("Nu se poate executa redo!")

        elif option == "x":
            break
        
        else:
            print("Ati ales o optiune gresita!")
        print()
