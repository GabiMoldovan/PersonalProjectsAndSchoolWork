from Domain.carte import Carte


class CarteValidator:
    def valideaza(self, carte: Carte):
        '''
        Clasa care valideaza o carte
        :param carte: cartea
        :return: None
        '''
        erori = []
        if carte.titlu == "":
            erori.append("Titlul este gol!")
        if carte.categorie not in ["beletristica", "sanatate", "istorie",
                                   "economie", "psihologie", "audiobook",
                                   "memorii", "tehnologie"]:
            erori.append("Cartea nu face parte dintr-o categorie valida")
        if int(carte.nrpg) <= int(0):
            erori.append("Cartea are un numar negativ sau nul de pagini!")
        if int(carte.pret) < int(0):
            erori.append("Pretul cartii este un numar negativ!")
        if int(len(carte.autori)) == int(0):
            erori.append("Cartea nu are autori!")
        if erori:
            raise ValueError(erori)
