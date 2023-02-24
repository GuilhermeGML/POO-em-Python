from dataclasses import dataclass


class OldPerson:
    def __init__(self, nome, lastname):
        self.nome = nome
        self.lastname = lastname

    def __str__(self):
        class_str = f'{self.__class__.__name__} ({self.nome} {self.lastname})'
        return class_str

    def __repr__(self):
        return str(self)

@dataclass
class Person:
    name: str
    lastname: str

if __name__ == '__main__':
    Jonh1 = Person('John', 'Doe')
    Jonh2 = Person('John', 'Doe')
    print(Jonh1)
    print(repr(Jonh1))
