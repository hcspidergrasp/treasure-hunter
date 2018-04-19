from system.metadata import LevelMetadata, ScenarioMetadata, ActionMetadata
from system.actions import Action, KeyValuePairChange
from system.scenario import Scenario
from system.level import Level

class LevelParser:
    
    __parsedLevel = None

    def parseLevel(self, path):
        fileHandler = open(path)
        levelMetadata = _parseLevelMetadata(fileHandler)
        scenarios = _parseScenarios(fileHandler, levelMetadata)
        self.__parsedLevel = Level(levelMetadata, scenarios)
        fileHandler.close()

    @property
    def parsedLevel(self):
        return self.__parsedLevel

# Functions

def _parseLevelMetadata(fileHandler):
    return LevelMetadata(*_readLineAndSplit(fileHandler))

def _parseScenarioMetadata(fileHandler): 
    rawMetadataLine = _readLineAndSplit(fileHandler)
    return ScenarioMetadata(*rawMetadataLine)

def _parseScenarioMessages(fileHandler, count):
    messages = list()
    i = 0
    while i < count:
        messages.append(fileHandler.readline())
        i += 1
    return messages

def _parseAction(fileHandler):
    rawAction = _readLineAndSplit(fileHandler)
    actionMetadata = ActionMetadata(*rawAction)
    inventoryChanges = "0"
    decisionChanges = "0"
    if actionMetadata.inventoryChange:
        rawInventory = _readLineAndSplit(fileHandler)
        inventoryChanges = (KeyValuePairChange(*_parseKeyValuePair(rawIC)) for rawIC in rawInventory)
    if actionMetadata.decisionChange:
        rawDecisions = _readLineAndSplit(fileHandler)
        decisionChanges = (KeyValuePairChange(*_parseKeyValuePair(rawDC)) for rawDC in rawDecisions)
    return Action(actionMetadata, inventoryChanges, decisionChanges)

def _parseActions(fileHandler, actionsCount):
    i = 0
    actions = list()
    while i < actionsCount:
        actions.append(_parseAction(fileHandler))
        i += 1
    return actions

def _parseKeyValuePair(rawString):
    return rawString.split("=")

def _readLineAndSplit(fileHandler):
    return fileHandler.readline().strip().split(" ")

def _parseScenario(fileHandler):
    metadata = _parseScenarioMetadata(fileHandler)
    messages = _parseScenarioMessages(fileHandler, metadata.messageCount)
    actions = _parseActions(fileHandler, metadata.actionCount)
    return Scenario(metadata, messages, actions)

def _parseScenarios(fileHandler, levelMetadata):
    scenarios = list()
    i = 0
    while i < levelMetadata.scenariosCount:
        scenarios.append(_parseScenario(fileHandler))
        i += 1
    return scenarios
