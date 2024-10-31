from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Rezervare(Entitate):
    '''
    Clasa pentru Rezervare
    '''
    idFilm: int
    idCardClient: int
    data: str
    ora: str
