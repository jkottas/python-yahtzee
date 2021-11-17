from random import Random
class Die:
    rand: Random = Random()
    
    def __init__(self, initialValue: int = None, sides: int = 6):
        self.__sides = sides
        if (initialValue is not None):
            self.__value = initialValue
        else:
            self.randomize()

    def setValue(self, newValue: int):
        self.__value = newValue

    def getValue(self):
        return self.__value

    def randomize(self):
        self.__value = Die.rand.randint(1, self.__sides)
        return self.__value

    def __str__(self):
        return f'{self.__value}'