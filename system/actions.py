from system.metadata import ActionMetadata
from typing import List


class KeyValuePairChange:

    def __init__(self, key, value):
        self.__key = key
        self.__value = value

    def apply(self, inventory):
        inventory[self.__key] = self.__value


class ActionResult:

    def __init__(self, state: int, level_to_switch: int):
        self.state: int = state
        self.levelToSwitch: int = level_to_switch


class Action:

    def __init__(self, metadata: ActionMetadata, inventory_changes: List[KeyValuePairChange],
                 decision_changes: List[KeyValuePairChange]):
        self.__metadata: ActionMetadata = metadata
        self.__inventory: List[KeyValuePairChange] = inventory_changes
        self.__decisions: List[KeyValuePairChange] = decision_changes

    @property
    def action_message(self) -> str:
        return self.__metadata.action_message

    def apply(self) -> ActionResult:
        return ActionResult(self.__metadata.level_state,
                            (self.__metadata.level_code if self.__metadata.level_change else None))
