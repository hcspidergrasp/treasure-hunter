class Inventory:

    def __init__(self):
        self._prisonKeys = False
        self._sunflowerSeeds = False
        self._guardiansMoney = False
        self._guardiansSword = False
        self._dragonsKey = False

    @property
    def prisonKeys(self):
        return self._prisonKeys

    @prisonKeys.setter
    def prisonKeys(self, value):
        self._prisonKeys = value

    @property
    def sunflowerSeeds(self):
        return self._sunflowerSeeds
    
    @sunflowerSeeds.setter
    def sunflowerSeeds(self, value):
        self._sunflowerSeeds = value

    @property
    def guardiansMoney(self):
        return self._guardiansMoney

    @guardiansMoney.setter
    def guardiansMoney(self, value):
        self._guardiansMoney

    @property
    def guardiansSword(self):
        return self._guardiansSword

    @guardiansSword.setter
    def guardiansSword(self, value):
        self._guardiansSword = value

    @property
    def dragonsKey(self):
        return self._dragonsKey

    @dragonsKey.setter
    def dragonsKey(self, value):
        self._dragonsKey = value
