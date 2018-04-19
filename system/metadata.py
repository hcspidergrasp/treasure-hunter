class LevelMetadata:

    __scenariosCount = None

    def __init__(self, scenariosCount):
        self.__scenariosCount = int(scenariosCount)

    @property
    def scenariosCount(self):
        return self.__scenariosCount

class ScenarioMetadata:
    
    __stateId = None
    __conditional = None
    __messageCount = None
    __actionCount = None

    def __init__(self, stateId, messageCount, actionCount):
        self.__stateId = int(stateId)
        self.__messageCount = int(messageCount)
        self.__actionCount = int(actionCount)

    @property
    def stateId(self):
        return self.__stateId

    @property
    def conditional(self):
        return self.__conditional

    @property
    def messageCount(self):
        return self.__messageCount

    @property
    def actionCount(self):
        return self.__actionCount

class ActionMetadata:
    
    __levelChange = None
    __levelState = None
    __levelCode = None
    __inventoryChange = None
    __decisionChange = None
    __actionMessage = None

    def __init__(self, levelChange, levelState, levelCode, inventoryChange, decisionChange, *actionMessage):
        self.__levelChange = bool(int(levelChange))
        self.__levelState = int(levelState)
        self.__levelCode = int(levelCode)
        self.__inventoryChange = bool(int(inventoryChange))
        self.__decisionChange = bool(int(decisionChange))
        self.__actionMessage = " ".join(actionMessage)

    @property
    def levelChange(self):
        return self.__levelChange

    @property
    def levelState(self):
        return self.__levelState

    @property
    def levelCode(self):
        return self.__levelCode

    @property
    def inventoryChange(self):
        return self.__inventoryChange
        
    @property
    def decisionChange(self):
        return self.__decisionChange

    @property
    def actionMessage(self):
        return self.__actionMessage