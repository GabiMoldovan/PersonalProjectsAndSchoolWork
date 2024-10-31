from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Carte(Entity):
    titlu: str
    categorie: str
    nrpg: int
    pret: int
    autori: list
