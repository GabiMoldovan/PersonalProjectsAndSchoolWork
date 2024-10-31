from Domain.film import Film
from Domain.filmError import FilmError


class ValideazaFilm:
    '''
    Clasa care valideaza filmul
    '''
    def valideazaFilmul(self, film: Film) -> None:
        '''
        Functia care verifica daca Filmul este corect
        :param film: Film
        :return: erorile daca exista vreo problema, altfel None
        '''
        erori = []
        if film.titlu == "":
            erori.append("Titlul filmului este gol")
        if film.idEntitate == "":
            erori.append("Id-ul filmului este gol")
        if film.anAparitie == "":
            erori.append("Anul aparitiei filmului este gol")
        if film.pretBilet == "":
            erori.append("Pretul biletului pentru film este gol")
        # if isinstance(film.inProgram, bool) is False:
        #    erori.append("Campul 'in program' trebuie sa fie True sau False")
        if len(erori) > 0:
            raise FilmError(erori)
