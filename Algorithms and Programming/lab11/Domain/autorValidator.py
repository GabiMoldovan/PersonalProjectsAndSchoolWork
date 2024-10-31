from Domain.autor import Autor


class AutorValidator:
    def valideaza(self, autor: Autor):
        '''
        Clasa care valideaza un autor
        :param autor: autorul
        :return: None
        '''
        erori = []
        if autor.nume == "":
            erori.append("Numele nu poate sa fie nul")
        if autor.prenume == "":
            erori.append("Prenumele nu poate sa fie nul")
        if autor.email == "":
            erori.append("Email-ul nu poate sa fie nul")
        if autor.email.find("@") == -1:
            erori.append("Email-ul nu contine caracterul @")
        if erori:
            raise ValueError(erori)
