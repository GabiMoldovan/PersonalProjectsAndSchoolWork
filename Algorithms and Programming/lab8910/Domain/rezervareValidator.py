from Domain.rezervare import Rezervare
from Domain.rezervareError import RezervareError


class ValideazaRezervare:
    '''
    Clasa care valideaza Rezervarea
    '''
    def valideazaRezervarea(self, rezervare: Rezervare) -> None:
        '''
        Functia care valideaza rezervarea
        :param rezervare: Rezervare
        :return: erorile daca exista vreo problema, altfel None
        '''
        erori = []
        getHour = rezervare.ora
        Hour = getHour[0] + getHour[1]
        if Hour >= str(24):
            erori.append("Ora data nu este corecta")
        if getHour[2] != ":" or len(getHour) > 5:
            erori.append("Formatul orei nu este"
                         " corect! (HH:MM)")
        getMins = getHour[3] + getHour[4]
        if getMins > "59":
            erori.append("Minutul nu poate sa fie mai mare decat 59!")
        getData = rezervare.data
        if getData[2] != "." or getData[5] != "." or len(getData) > 10:
            erori.append("Nu ati dat un format "
                         "corect al datei! (dd.mm.yyyy)")

        if len(erori) > 0:
            raise RezervareError(erori)
