from dataclasses import dataclass


@dataclass
class linkError(Exception):
    message: any

    def __str__(self):
        return f'Link error: {self.message}'
