from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class CardClient(Entitate):
    '''
    Clasa pentru Card
    '''
    nume: str
    prenume: str
    CNP: str
    dataNasterii: str
    dataInregistrarii: str
    puncte: int
