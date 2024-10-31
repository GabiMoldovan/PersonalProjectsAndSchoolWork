from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Film(Entitate):
    '''
    Clasa pentru Film
    '''
    titlu: str
    anAparitie: int
    pretBilet: int
    inProgram: bool
