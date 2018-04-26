from system.metadata import ScenarioMetadata
from system.actions import Action
from typing import List, Iterable

class Scenario:

    def __init__(self, metadata: ScenarioMetadata, messages: List[str], actions: List[Action]):
        self.__metadata: ScenarioMetadata = metadata
        self.__messages: List[str] = messages
        self.__actions: List[Action] = actions

    @property
    def stateId(self) -> int:
        return self.__metadata.stateId

    def messageSequence(self) -> Iterable[str]:
        for message in self.__messages:
            yield message

    def actionsSequence(self) -> Iterable[str]:
        i = 1
        for action in self.__actions:
            yield "{0}. {1}".format(i, action.actionMessage)
            i += 1
            
    def getActionById(self, actionId: int) -> Action:
        return self.__actions[actionId]
