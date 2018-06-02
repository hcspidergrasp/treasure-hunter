from system.metadata import LevelMetadata, ScenarioMetadata, ActionMetadata
from system.actions import Action, KeyValuePairChange
from system.scenario import Scenario
from system.level import Level


class LevelParser:
    __parsedLevel: Level = None

    def parse_level(self, path):
        file_handler = open(path)
        level_metadata = _parse_level_metadata(file_handler)
        scenarios = _parse_scenarios(file_handler, level_metadata)
        self.__parsedLevel = Level(level_metadata, scenarios)
        file_handler.close()

    @property
    def parsed_level(self) -> Level:
        return self.__parsedLevel


# Functions

def _parse_level_metadata(file_handler):
    return LevelMetadata(*_read_line_and_split(file_handler))


def _parse_scenario_metadata(file_handler):
    raw_metadata_line = _read_line_and_split(file_handler)
    return ScenarioMetadata(*raw_metadata_line)


def _parse_scenario_messages(file_handler, count):
    messages = list()
    i = 0
    while i < count:
        messages.append(file_handler.readline())
        i += 1
    return messages


def _parse_action(file_handler):
    raw_action = _read_line_and_split(file_handler)
    action_metadata = ActionMetadata(*raw_action)
    inventory_changes = "0"
    decision_changes = "0"
    if action_metadata.inventory_change:
        raw_inventory = _read_line_and_split(file_handler)
        inventory_changes = (KeyValuePairChange(*_parse_key_value_pair(rawIC)) for rawIC in raw_inventory)
    if action_metadata.decision_change:
        raw_decisions = _read_line_and_split(file_handler)
        decision_changes = (KeyValuePairChange(*_parse_key_value_pair(rawDC)) for rawDC in raw_decisions)
    return Action(action_metadata, inventory_changes, decision_changes)


def _parse_actions(file_handler, actions_count):
    i = 0
    actions = list()
    while i < actions_count:
        actions.append(_parse_action(file_handler))
        i += 1
    return actions


def _parse_key_value_pair(raw_string):
    return raw_string.split("=")


def _read_line_and_split(file_handler):
    return file_handler.readline().strip().split(" ")


def _parse_scenario(file_handler):
    metadata = _parse_scenario_metadata(file_handler)
    messages = _parse_scenario_messages(file_handler, metadata.message_count)
    actions = _parse_actions(file_handler, metadata.action_count)
    return Scenario(metadata, messages, actions)


def _parse_scenarios(file_handler, level_metadata):
    scenarios = list()
    i = 0
    while i < level_metadata.scenarios_count:
        scenarios.append(_parse_scenario(file_handler))
        i += 1
    return scenarios
