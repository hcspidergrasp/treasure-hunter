class Action:

    def __init__(self, metadata, inventoryChanges, decisionChanges):
        self.__metadata = metadata
        self.__inventory = inventoryChanges
        self.__decisions = decisionChanges

class KeyValuePairChange:

    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def apply(self, inventory):
        inventory[self.__key] = self.__value
