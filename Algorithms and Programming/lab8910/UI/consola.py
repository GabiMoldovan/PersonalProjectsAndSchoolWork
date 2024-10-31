from random import randint
import random
import string
from time import strptime
from xmlrpc.client import DateTime

from Domain.IncrementOperation import IncrementOperation
from Domain.card import CardClient
from Domain.cardError import CardError
from Domain.cascadeDeleteOperation import CascadeDeleteOperation
from Domain.deleteAllGenerated import DeleteAllGenerated
from Domain.filmError import FilmError
from Domain.rezervareError import RezervareError
from Repository.repository import Repository
from Service.timeManager import checkValidHour
from Service.cardService import CardService
from Service.filmService import FilmService
from Service.rezervareService import RezervareService
from Service.undoRedoService import UndoRedoService


class Consola:
    '''
    TODO
    asana
    task live la lab
    '''
    def __init__(self,
                 cardService: CardService,
                 filmService: FilmService,
                 cardRepository: Repository,
                 rezervareService: RezervareService,
                 undoRedoService: UndoRedoService,
                 rezervareRepository: Repository) -> None:
        '''
        Pasarea parametrilor
        :param cardService: parametrul care tine CardService
        :param filmService: parametrul care tine FilmService
        :param rezervareService: parametrul care tine RezervareService
        '''
        self.__cardService = cardService
        self.__filmService = filmService
        self.__rezervareService = rezervareService
        self.__undoRedoService = undoRedoService
        self.__cardRepository = cardRepository
        self.__rezervareRepository = rezervareRepository

    def runMenu(self) -> None:
        '''
        Main menu
        :return: None
        '''
        while True:
            print("1. CRUD carduri")
            print("2. CRUD filme")
            print("3. CRUD rezervari")
            print("4. Afiseaza cardurile/filmele "
                  "in care campurile contin un anumit text")
            print("5. Genereaza un numar de carduri client")
            print("6. Afiseaza rezervarile dintr-un interval de ore dat")
            print("7. Afiseaza filmele"
                  " ordonate descrescator dupa nr de rezervari")
            print("8. Afiseaza cardurile in"
                  " ordine descrescatoare dupa nr puncte de pe card")
            print("9. Sterge rezervarile dintr-un anumit interval de zile")
            print("10. Incrementarea punctelor de pe cardurile cu ziua "
                  "de nastere dintr-un interval dat")
            print("u. Undo")
            print("r. Redo")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.runCRUDCarduriMenu()

            elif optiune == "2":
                self.runCRUDFilmeMenu()

            elif optiune == "3":
                self.runCRUDRezervariMenu()

            elif optiune == "4":
                text = input("Dati textul: ")
                rezultat = []
                rezultat.append(
                    self.__cardService.fullTextSearchInCard(text))
                rezultat.append(
                    self.__filmService.fullTextSearchInFilme(text))
                for element in rezultat:
                    print(element)

            elif optiune == "5":
                listaCarduriNoi = []
                while True:
                    try:
                        n = int(input("Dati numarul de carduri "
                                      "pentru generare: "))
                        break
                    except ValueError:
                        print("Dati un numar natural de carduri!")
                while n > 0:
                    idCard = randint(1, 99999)
                    carduri = self.__cardService.getAll()
                    IDuri = []
                    for card in carduri:
                        IDuri.append(card.idEntitate)
                    while idCard in IDuri:
                        idCard = randint(1, 99999)
                    IDuri.append(idCard)
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
                    self.__cardService.adauga(
                        str(idCard), nume, prenume, CNP,
                        dataNasterii, dataInregistrarii, puncte)
                    listaCarduriNoi.append(CardClient(
                        str(idCard), nume, prenume, CNP,
                        dataNasterii, dataInregistrarii, puncte))
                    n = n - 1
                self.__undoRedoService.addUndoOperation(
                    DeleteAllGenerated(self.__cardRepository, listaCarduriNoi))

            elif optiune == "6":
                oraSt = input("Dati prima ora (hh:mm): ")
                while checkValidHour(oraSt) is False:
                    oraSt = input("Prima ora"
                                  " are un format gresit, dati alta ora: ")
                oraDr = input("Dati a doua ora: ")
                while checkValidHour(oraDr) is False:
                    oraDr = input("A doua ora"
                                  " are un format gresit, dati alta ora: ")
                rez = self.uiAfiseazaRezervariIntervalOrar(oraSt, oraDr)
                for rezervare in rez:
                    print(rezervare)

            elif optiune == "7":
                listaIdFilme = []
                listaTitluri = []
                rez = self.uiGetFilmeDescrDupaRezervari()
                for idulfilmului in rez:
                    for film in self.__filmService.getAll():
                        if film.idEntitate == idulfilmului:
                            listaIdFilme.append(idulfilmului)
                            listaTitluri.append(film.titlu)
                print(list(zip(listaIdFilme, listaTitluri)))

            elif optiune == "8":
                rez = self.uiGetCarduriDescrDupaNrPct()
                for pct in rez:
                    for card in self.__cardService.getAll():
                        if card.puncte == pct:
                            print(card)
            elif optiune == "9":
                ziUnu = input("Dati prima zi: ")
                while ziUnu < "0" and ziUnu > "31":
                    ziUnu = input("Ziua unu este prea"
                                  " mica sau prea mare, dati alta: ")
                ziDoi = input("Dati a doua zi: ")
                while ziDoi < "0" and ziDoi > "31":
                    ziDoi = input("Ziua doi este prea"
                                  " mica sau prea mare, dati alta: ")
                if ziUnu > ziDoi:
                    forSwap = ziUnu
                    ziUnu = ziDoi
                    ziDoi = forSwap
                lenRez = int(0)
                for i in self.__rezervareService.getAll():
                    lenRez += int(1)
                listaRez = []
                self.__rezervareService.stergeRezervariIntervalZile(ziUnu,
                                                                    ziDoi,
                                                                    lenRez,
                                                                    listaRez)

            elif optiune == "10":
                dataUnu = None
                dataDoi = None
                nrPct = None
                try:
                    nrPct = int(input("Dati numarul de puncte: "))
                    dataUnu = DateTime(strptime(input("Dati"
                                                      " data unu: "
                                                      ""), "%d.%m.%Y"
                                                ))
                    dataDoi = DateTime(strptime(input("Dati"
                                                      " data doi: "
                                                      ""), "%d.%m.%Y"
                                                ))
                except ValueError as ve:
                    print(ve)
                self.uiIncrementarePctCard(nrPct, dataUnu, dataDoi)

            elif optiune == "u":
                self.__undoRedoService.undo()

            elif optiune == "r":
                self.__undoRedoService.redo()

            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDCarduriMenu(self) -> None:
        '''
        Menu card
        :return: None
        '''
        while True:
            print("1. Adauga card")
            print("2. Sterge card")
            print("3. Modifica card")
            print("a. Afiseaza toate cardurile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaCard()
            elif optiune == "2":
                self.uiStergeCard()
            elif optiune == "3":
                self.uiModificaCard()
            elif optiune == "a":
                self.showAllCarduri()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDFilmeMenu(self) -> None:
        '''
        Menu film
        :return: None
        '''
        while True:
            print("1. Adauga film")
            print("2. Sterge film")
            print("3. Modifica film")
            print("a. Afiseaza toate filmele")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaFilm()
            elif optiune == "2":
                self.uiStergeFilm()
            elif optiune == "3":
                self.uiModificaFilm()
            elif optiune == "a":
                self.showAllFilme()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaCard(self) -> None:
        '''
        Functia UI pentru adaugarea unui card
        :return: None
        '''
        try:
            idCard = input("Dati id-ul cardului: ")
            nume = input("Dati numele proprietarului: ")
            prenume = input("Dati prenumele proprietarului: ")
            CNP = input("Dati CNP-ul proprietarului: ")
            dataNasterii = DateTime(strptime(input("Dati "
                                                   "data nasterii:"
                                                   " "), "%d.%m.%Y"))
            dataInregistrarii = input("Dati data inregistrarii: ")
            puncte = input("Dati numarul de puncte: ")
            dataNasterii = str(dataNasterii)
            dataNasteriiToString = dataNasterii[6] + \
                dataNasterii[7] + "." + \
                dataNasterii[4] + \
                dataNasterii[5] + "." + \
                dataNasterii[0] + \
                dataNasterii[1] + \
                dataNasterii[2] + \
                dataNasterii[3]
            self.__cardService.adauga(
                idCard, nume, prenume, CNP,
                dataNasteriiToString, dataInregistrarii,
                puncte)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except CardError as ce:
            print(ce)
        except Exception as e:
            print(e)

    def uiStergeCard(self) -> None:
        '''
        Functia UI pentru stergerea unui card
        :return: None
        '''
        carduriSterse = []
        rezervariSterse = []
        try:
            idCardSterge = input("Dati id-ul cardului de sters: ")
            for card in self.__cardRepository.read():
                if card.idEntitate == idCardSterge:
                    carduriSterse.append(card)
                    self.__cardService.sterge(idCardSterge)
        except KeyError as ke:
            print(ke)
        except CardError as ce:
            print(ce)
        except Exception as e:
            print(e)
        self.__rezervareService.stergeCards(idCardSterge, rezervariSterse)
        self.__undoRedoService.addUndoOperation(CascadeDeleteOperation(
            self.__cardRepository,
            self.__rezervareRepository,
            carduriSterse,
            rezervariSterse))

    def uiModificaCard(self) -> None:
        '''
        Functia UI pentru modificarea unui card
        :return: None
        '''
        try:
            idCard = input("Dati id-ul cardului de modificat: ")
            nume = input("Dati numele proprietarului de modificat: ")
            prenume = input("Dati prenumele proprietarului de modificat: ")
            CNP = input("Dati CNP-ul proprietarului de modificat: ")
            dataNasterii = DateTime(strptime(input("Dati data "
                                                   "nasterii de modificat: "),
                                             "%d.%m.%Y"))
            dataInregistrarii = input("Dati data inregistrarii de "
                                      "modificat: ")
            puncte = input("Dati numarul de puncte de modificat: ")

            dataNasterii = str(dataNasterii)
            dataNasteriiToString = dataNasterii[6] + \
                dataNasterii[7] + "." + \
                dataNasterii[4] + \
                dataNasterii[5] + "." + \
                dataNasterii[0] + \
                dataNasterii[1] + \
                dataNasterii[2] + \
                dataNasterii[3]

            self.__cardService.modifica(
                idCard, nume, prenume, CNP,
                dataNasteriiToString, dataInregistrarii,
                puncte)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except CardError as ce:
            print(ce)
        except Exception as e:
            print(e)

    def showAllCarduri(self) -> None:
        '''
        Afiseaza toate cardurile
        :return: None
        '''
        for card in self.__cardService.getAll():
            print(card)

    def uiAdaugaFilm(self) -> None:
        '''
        Functia UI pt adaugarea unui film
        :return: None
        '''
        try:
            idFilm = input("Dat id-ul filmului: ")
            titlu = input("Dati titlul filmului: ")
            anAparitie = input("Dati anul aparitiei filmului: ")
            pretBilet = input("Dati pretul biletului: ")
            inProgram = input("Dati daca este in program(True/False): ")

            self.__filmService.adauga(
                idFilm, titlu, anAparitie, pretBilet, inProgram)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except FilmError as fe:
            print(fe)
        except Exception as e:
            print(e)

    def uiStergeFilm(self) -> None:
        '''
        Functia UI pt stergerea unui film
        :return: None
        '''
        try:
            idFilm = input("Dati id-ul filmului de sters: ")

            self.__filmService.sterge(idFilm)
        except KeyError as ke:
            print(ke)
        except FilmError as fe:
            print(fe)
        except Exception as e:
            print(e)

    def uiModificaFilm(self) -> None:
        '''
        Functia UI pt modificarea unui film
        :return: None
        '''
        try:
            idFilm = input("Dat id-ul filmului de modificat: ")
            titlu = input("Dati titlul filmului de modificat: ")
            anAparitie = input("Dati anul aparitiei filmului de modificat: ")
            pretBilet = input("Dati pretul biletului de modificat: ")
            inProgram = input("Dati daca este in "
                              "program(True/False) de modificat: ")

            self.__filmService.modifica(
                idFilm, titlu, anAparitie, pretBilet, inProgram)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except FilmError as fe:
            print(fe)
        except Exception as e:
            print(e)

    def showAllFilme(self) -> None:
        '''
        Afiseaza toate filmele
        :return: None
        '''
        for film in self.__filmService.getAll():
            print(film)

    def runCRUDRezervariMenu(self) -> None:
        '''
        Menu rezervare
        :return: None
        '''
        while True:
            print("1. Adauga rezervare")
            print("2. Sterge rezervare")
            print("3. Modifica rezervare")
            print("a. Afiseaza toate rezervarile")
            print("x. Iesire")
            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.uiAdaugaRezervare()
            elif optiune == "2":
                self.uiStergeRezervare()
            elif optiune == "3":
                self.uiModificaRezervare()
            elif optiune == "a":
                self.showAllRezervari()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaRezervare(self) -> None:
        '''
        Ui pt adaugare rezervare
        :return: None
        '''
        try:
            idRezervare = input("Dati id-ul rezervarii: ")
            idFilmm = input("Dati id-ul filmului: ")
            idCardClient = input("Dati id-ul cardului clientului: ")
            data = DateTime(strptime(input("Dati data: "), "%d.%m.%Y"))
            ora = input("Dati ora: ")

            data = str(data)
            dataToString = data[6] + \
                data[7] + "." + \
                data[4] + \
                data[5] + "." + \
                data[0] + \
                data[1] + \
                data[2] + \
                data[3]

            for film in self.__filmService.getAll():
                if film.inProgram != "True" and \
                        film.idEntitate == idFilmm:
                    print("Filmul nu este in program!")
                    return

            self.__rezervareService.adauga(
                idRezervare,
                idFilmm,
                idCardClient,
                dataToString,
                ora)
            self.__cardService.aplicaPuncte(idCardClient, idFilmm)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except RezervareError as re:
            print(re)
        except Exception as e:
            print(e)

    def uiStergeRezervare(self) -> None:
        '''
        Fct UI pt stergerea unei rezervari
        :return: None
        '''
        try:
            idRezervare = input("Dati id-ul rezervarii de sters: ")

            self.__rezervareService.sterge(idRezervare)
        except KeyError as ke:
            print(ke)
        except RezervareError as re:
            print(re)
        except Exception as e:
            print(e)

    def uiModificaRezervare(self) -> None:
        '''
        Fct UI pt modificarea unei rezervari
        :return: None
        '''
        try:
            idRezervare = input("Dati id-ul rezervarii de modificat: ")
            idFilm = input("Dati id-ul filmului de modificat: ")
            idCardClient = input("Dati id-ul "
                                 "cardului clientului de modificat: ")
            data = DateTime(strptime(input("Dati data de "
                                           "modificat: "), "%d.%m.%Y"))
            ora = input("Dati ora de modificat: ")

            data = str(data)
            dataToString = data[6] + \
                data[7] + "." + \
                data[4] + \
                data[5] + "." + \
                data[0] + \
                data[1] + \
                data[2] + \
                data[3]

            self.__rezervareService.modifica(
                idRezervare,
                idFilm,
                idCardClient,
                dataToString,
                ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except RezervareError as re:
            print(re)
        except Exception as e:
            print(e)

    def showAllRezervari(self) -> None:
        '''
        Afiseaza toate rezervarile
        :return:
        '''
        for rezervare in self.__rezervareService.getAll():
            print(rezervare)

    def uiAfiseazaRezervariIntervalOrar(self, oraSt, oraDr) -> list:
        '''
        Determina rezervarile dintr-un interval orar
        :param oraSt: primul capat al intervalului
        :param oraDr: al doilea capat al intervalului
        :return: lista de rezervari
        '''
        hourSt = oraSt[0] + oraSt[1]
        hourDr = oraDr[0] + oraDr[1]
        minSt = oraSt[3] + oraSt[4]
        minDr = oraDr[3] + oraDr[4]

        rezultat = []

        for rezervare in self.__rezervareService.getAll():
            oraRezervare = rezervare.ora
            hourRez = oraRezervare[0] + oraRezervare[1]
            minRez = oraRezervare[3] + oraRezervare[4]
            rezultat.append(list(rezervareDoi for rezervareDoi in
                            self.__rezervareService.getAll() if
                            hourRez >= hourSt and hourRez <= hourDr and
                                 minRez >= minSt and minRez <= minDr and
                            rezervare.idEntitate == rezervareDoi.idEntitate))
            # if hourRez >= hourSt and hourRez <= hourDr and \
            #        minRez >= minSt and minRez <= minDr:
            #    rezultat.append(rezervare)
        return rezultat

    def uiGetFilmeDescrDupaRezervari(self) -> list:
        '''
        :return: lista de filme ordonata descrescator dupa nr de rezervari
        '''
        rez = []
        for film in self.__rezervareService.ordoneazaFilmeDupaRezervari():
            rez.append(film)
        return rez

    def uiGetCarduriDescrDupaNrPct(self) -> list:
        '''
        :return: lista de carduri ordonata descrescator dupa nr de puncte
        '''
        rez = []
        for card in self.__cardService.uiGetCarduriDescrDupaNrPct():
            rez.append(card)
        return rez

    def uiIncrementarePctCard(self, nrPct, dataUnu, dataDoi) -> None:
        '''
        incrementeaza cardurile dintr-un interval orar cu un numar de puncte
        :param nrPct: numarul de puncte
        :param dataUnu: primul capat al intervalului orar
        :param dataDoi: al doilea capat al intervalului orar
        :return: None
        '''

        carduriVechi = []
        carduriNoi = []

        cardValid = []
        cardValid = self.__cardService.getBDayCardsFromInterval(dataUnu,
                                                                dataDoi)
        for id in cardValid:
            for card in self.__cardService.getAll():
                if card.idEntitate == id:

                    carduriVechi.append(CardClient(card.idEntitate,
                                                   card.nume,
                                                   card.prenume,
                                                   card.CNP,
                                                   card.dataNasterii,
                                                   card.dataInregistrarii,
                                                   int(card.puncte)))

                    self.__cardService.modifica(
                        card.idEntitate, card.nume,
                        card.prenume,
                        card.CNP,
                        card.dataNasterii,
                        card.dataInregistrarii,
                        int(card.puncte)
                        +
                        int(nrPct))

                    carduriNoi.append(CardClient(card.idEntitate,
                                                 card.nume,
                                                 card.prenume,
                                                 card.CNP,
                                                 card.dataNasterii,
                                                 card.dataInregistrarii,
                                                 int(card.puncte)
                                                 +
                                                 int(nrPct)))
        self.__undoRedoService.addUndoOperation(IncrementOperation(
            self.__cardRepository, carduriVechi, carduriNoi)
        )
