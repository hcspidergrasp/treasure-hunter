from system.scenario import Scenario

class GameUI:

    def __printScenarioMessages(self, scenario: Scenario):
        print("\n")
        for message in scenario.messageSequence():
            print(message)

    def __printScenarioActions(self, scenario: Scenario):
        for action in scenario.actionsSequence():
            print(action)

    def __requestActionFromUser(self) -> int:
        actionNumber = input("-> ")
        return int(actionNumber) - 1

    def printScenarioAndRequestAction(self, scenario: Scenario) -> int:
        self.__printScenarioMessages(scenario)
        self.__printScenarioActions(scenario)
        return self.__requestActionFromUser()
