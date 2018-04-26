from system.metadata import ActionMetadata
from typing import List

class KeyValuePairChange:

    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def apply(self, inventory):
        inventory[self.__key] = self.__value

class ActionResult:
    
    def __init__(self, state: int, levelToSwitch: int):
        self.state: int = state
        self.levelToSwitch: int = levelToSwitch

class Action:

    def __init__(self, metadata: ActionMetadata, inventoryChanges: List[KeyValuePairChange], decisionChanges: List[KeyValuePairChange]):
        self.__metadata: ActionMetadata = metadata
        self.__inventory: List[KeyValuePairChange] = inventoryChanges
        self.__decisions: List[KeyValuePairChange] = decisionChanges

    @property
    def actionMessage(self) -> str:
        return self.__metadata.actionMessage

    def apply(self) -> ActionResult:
        return ActionResult(self.__metadata.levelState, (self.__metadata.levelCode if self.__metadata.levelChange else None))
