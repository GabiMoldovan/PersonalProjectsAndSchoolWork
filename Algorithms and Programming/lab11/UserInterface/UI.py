from Service.carteService import CarteService
from Service.autorService import AutorService


class Console:
    def __init__(self, carteService: CarteService,
                 autorService: AutorService):
        self.carteService = carteService
        self.autorService = autorService

    def runMenu(self):
        '''
        Meniul cu utilizatorul
        :return: None
        '''
        while True:
            print("1. Adauga carte")
            print("2. Adauga autor")
            print("3. Afiseaza cartile de tip audiobook in ordine alfabetica")
            print("4. Afisarea pretului maxim si "
                  "nr mediu de pagini pt cartile din fiecare categorie")
            print("a1. Afiseaza cartile")
            print("a2. Afiseaza autori")
            print("x. Iesire")

            optiune = input("Dati optiunea: ")

            if optiune == "1":
                self.adaugaCarte()
            elif optiune == "2":
                self.adaugaAutor()
            elif optiune == "3":
                self.printAplhabeticallyAudioBooks()
            elif optiune == "4":
                self.printMaxPriceAndAveragePagesForCategoryBooks()
            elif optiune == "a1":
                self.afiseaza(self.carteService.getAll())
            elif optiune == "a2":
                self.afiseaza(self.autorService.getAll())
            elif optiune == "x":
                break

            else:
                print("Ati dat o optiune gresita!")

    def afiseaza(self, entitati):
        '''
        Functia care afiseaza toate obiectele unei entitati
        :param entitati: Entitatea
        :return: None
        '''
        for entitate in entitati:
            print(entitate)

    def adaugaCarte(self):
        '''
        Functia UI pentru adaugarea unei carti
        :return:
        '''
        try:
            idCarte = input("Dati id-ul cartii: ")
            titlu = input("Dati titlul cartii: ")
            categorie = input("Dati categoria cartii 'beletristica', "
                              "'sanatate', 'istorie',"
                              "'economie', 'psihologie', 'audiobook',"
                              "'memorii', 'tehnologie': ")
            nrpg = int(input("Dati nr paginilor: "))
            pret = int(input("Dati pretul: "))
            nrAutori = int(input("Dati nr de autori: "))
            listaid = []
            exista = False
            while exista is False:
                for i in range(0, nrAutori):
                    idAutor = input("Dati id-ul autorului: ")
                    for autori in self.autorService.getAll():
                        if autori.id_entity == idAutor:
                            exista = True
                    if exista is True:
                        listaid.append(idAutor)
                    else:
                        listaid = []
                        print("Nu exista autorul cu acest id")
                        break
            self.carteService.adauga(idCarte, titlu, categorie, nrpg,
                                     pret, listaid)
        except Exception as e:
            print(e)

    def adaugaAutor(self):
        '''
        Functia UI pentru adaugarea unui autor
        :return: None
        '''
        try:
            idAutor = input("Dati id-ul autorului: ")
            nume = input("Dati numele autorului: ")
            prenume = input("Dati prenumele autorului: ")
            email = input("Dati email-ul autorului: ")
            self.autorService.adauga(idAutor, nume, prenume, email)
        except Exception as e:
            print(e)

    def printAplhabeticallyAudioBooks(self):
        '''
        Afiseaza o lista a cartilor de categoria audiobook
        in ordine alfabetica dupa titlu
        :return: None
        '''
        listaCarti = []
        listaTitluri = []
        for carti in self.carteService.getAll():
            if carti.categorie == "audiobook":
                listaCarti.append(carti)
                listaTitluri.append(carti.titlu)

        ok = True
        while ok is True:
            ok = False
            for id in range(1, int(len(listaCarti))):
                if listaTitluri[id] < listaTitluri[id-1]:
                    ok = True
                    holder = listaCarti[id]
                    listaCarti[id] = listaCarti[id-1]
                    listaCarti[id-1] = holder
                    holder = listaTitluri[id]
                    listaTitluri[id] = listaTitluri[id-1]
                    listaTitluri[id-1] = holder
        for carte in listaCarti:
            print(carte)

    def printMaxPriceAndAveragePagesForCategoryBooks(self):
        categorii = ["beletristica", "sanatate", "istorie",
                     "economie", "psihologie", "audiobook",
                     "memorii", "tehnologie"]

        for categorie in categorii:
            pretMax = None
            nrPg = int(0)
            nrCarti = int(0)
            for carti in self.carteService.getAll():
                if carti.categorie == categorie:
                    if pretMax is None:
                        pretMax = carti.pret
                    if pretMax < carti.pret:
                        pretMax = carti.pret
                    nrCarti = nrCarti + int(1)
                    nrPg = nrPg + int(carti.nrpg)
            if pretMax is not None:
                print("Pret/Medie pagini pt categoria " +
                      categorie, end=": ")
                print(pretMax, end=" ")
                print(int(nrPg//nrCarti))
