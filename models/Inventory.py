class Inventory:

    def __init__(self):
        self._prisonKeys = False
        self._sunflowerSeeds = False
        self._guardiansMoney = False
        self._guardiansSword = False
        self._dragonsKey = False

    @property
    def prison_keys(self):
        return self._prisonKeys

    @prison_keys.setter
    def prison_keys(self, value):
        self._prisonKeys = value

    @property
    def sunflower_seeds(self):
        return self._sunflowerSeeds
    
    @sunflower_seeds.setter
    def sunflower_seeds(self, value):
        self._sunflowerSeeds = value

    @property
    def guardians_money(self):
        return self._guardiansMoney

    @guardians_money.setter
    def guardians_money(self, value):
        self._guardiansMoney

    @property
    def guardians_sword(self):
        return self._guardiansSword

    @guardians_sword.setter
    def guardians_sword(self, value):
        self._guardiansSword = value

    @property
    def dragons_key(self):
        return self._dragonsKey

    @dragons_key.setter
    def dragons_key(self, value):
        self._dragonsKey = value
