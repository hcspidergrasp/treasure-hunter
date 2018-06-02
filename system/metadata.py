class LevelMetadata:
    __scenariosCount = None

    def __init__(self, scenarios_count):
        self.__scenariosCount = int(scenarios_count)

    @property
    def scenarios_count(self):
        return self.__scenariosCount


class ScenarioMetadata:
    __stateId = None
    __conditional = None
    __messageCount = None
    __actionCount = None

    def __init__(self, state_id, message_count, action_count):
        self.__stateId = int(state_id)
        self.__messageCount = int(message_count)
        self.__actionCount = int(action_count)

    @property
    def state_id(self):
        return self.__stateId

    @property
    def conditional(self):
        return self.__conditional

    @property
    def message_count(self):
        return self.__messageCount

    @property
    def action_count(self):
        return self.__actionCount


class ActionMetadata:
    __levelChange = None
    __levelState = None
    __levelCode = None
    __inventoryChange = None
    __decisionChange = None
    __actionMessage = None

    def __init__(self, level_change, level_state, level_code, inventory_change, decision_change, *action_message):
        self.__levelChange = bool(int(level_change))
        self.__levelState = int(level_state)
        self.__levelCode = int(level_code)
        self.__inventoryChange = bool(int(inventory_change))
        self.__decisionChange = bool(int(decision_change))
        self.__actionMessage = " ".join(action_message)

    @property
    def level_change(self):
        return self.__levelChange

    @property
    def level_state(self):
        return self.__levelState

    @property
    def level_code(self):
        return self.__levelCode

    @property
    def inventory_change(self):
        return self.__inventoryChange

    @property
    def decision_change(self):
        return self.__decisionChange

    @property
    def action_message(self):
        return self.__actionMessage
