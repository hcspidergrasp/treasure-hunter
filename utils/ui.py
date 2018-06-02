from system.scenario import Scenario


class GameUI:

    def __print_scenario_messages(self, scenario: Scenario):
        print("\n")
        for message in scenario.message_sequence():
            print(message)

    def __print_scenario_actions(self, scenario: Scenario):
        for action in scenario.actions_sequence():
            print(action)

    def __request_action_from_user(self) -> int:
        action_number = input("-> ")
        return int(action_number) - 1

    def print_scenario_and_request_action(self, scenario: Scenario) -> int:
        self.__print_scenario_messages(scenario)
        self.__print_scenario_actions(scenario)
        return self.__request_action_from_user()
