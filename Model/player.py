from Model.die import Die

class Player:

    def __init__(self, name: str, numberOfDice: int):
        self.__name = name
        self.__dice = [Die() for i in range(numberOfDice)]

    def __str__(self):
        return f'{self.__name}: {[x.getValue() for x in self.__dice]}'