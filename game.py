from system.actions import ActionResult
from system.level import Level
from utils.levels import LevelCodes
from utils.parser import LevelParser
from utils.ui import GameUI

LEVEL_CODES_FILE_PATH = "assets/levels.dat"
START_LEVEL_CODE = 100

levelCodes = LevelCodes(LEVEL_CODES_FILE_PATH)
gameUI = GameUI()


def load_level(level) -> Level:
    level_parser = LevelParser()
    level_parser.parse_level(levelCodes.resolve_level_file_by_code(level))
    return level_parser.parsed_level


def get_last_level_state(level) -> int:
    global levelStateMap
    try:
        return levelStateMap[level]
    finally:
        return 1


def play_level(level: Level, state: int) -> ActionResult:
    global gameUI
    # noinspection PyTypeChecker
    result = ActionResult(state, None)
    while True:
        scenario = level.get_scenario_by_state(result.state)
        action_id = gameUI.print_scenario_and_request_action(scenario)
        result: ActionResult = scenario.get_action_by_id(action_id).apply()
        if result.levelToSwitch is not None:
            break
    return result


def cache_level_results(result: ActionResult):
    global levelStateMap
    global current_level_code
    levelStateMap[result.levelToSwitch] = result.state
    current_level_code = result.levelToSwitch


# Gameplay

current_level_code = START_LEVEL_CODE
levelStateMap = {}
while current_level_code > 1:
    currentLevel = load_level(current_level_code)
    current_level_state = get_last_level_state(current_level_code)
    levelResult: ActionResult = play_level(currentLevel, current_level_state)
    cache_level_results(levelResult)
