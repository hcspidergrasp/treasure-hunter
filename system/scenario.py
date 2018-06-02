from system.metadata import ScenarioMetadata
from system.actions import Action
from typing import List, Iterable


class Scenario:

    def __init__(self, metadata: ScenarioMetadata, messages: List[str], actions: List[Action]):
        self.__metadata: ScenarioMetadata = metadata
        self.__messages: List[str] = messages
        self.__actions: List[Action] = actions

    @property
    def state_id(self) -> int:
        return self.__metadata.state_id

    def message_sequence(self) -> Iterable[str]:
        for message in self.__messages:
            yield message

    def actions_sequence(self) -> Iterable[str]:
        i = 1
        for action in self.__actions:
            yield "{0}. {1}".format(i, action.action_message)
            i += 1

    def get_action_by_id(self, action_id: int) -> Action:
        return self.__actions[action_id]
