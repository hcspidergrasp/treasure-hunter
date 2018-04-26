from utils.levels import LevelCodes
from utils.parser import LevelParser
from utils.ui import GameUI
from system.level import Level
from system.scenario import Scenario
from system.actions import ActionResult

LEVEL_CODES_FILE_PATH = "assets/levels.dat"
START_LEVEL_CODE = 100

levelCodes = LevelCodes(LEVEL_CODES_FILE_PATH)
gameUI = GameUI()

def loadLevel(level) -> Level:
    levelParser = LevelParser()
    levelParser.parseLevel(levelCodes.resolveLevelFileByCode(level))
    return levelParser.parsedLevel

def getLastLevelState(level) -> int:
    global levelStateMap
    try:
        return levelStateMap[level]
    finally:
        return 1

def playLevel(level: Level, state: int) -> ActionResult:
    global gameUI
    result = ActionResult(state, None)
    while True:
        scenario = level.getScenarioByState(result.state)
        actionId = gameUI.printScenarioAndRequestAction(scenario)
        result: ActionResult = scenario.getActionById(actionId).apply()
        if result.levelToSwitch is not None:
            break
    return result

def cacheLevelResults(result: ActionResult):
    global levelStateMap
    global level
    levelStateMap[result.levelToSwitch] = result.state
    level = result.levelToSwitch

# Gameplay

level = START_LEVEL_CODE
levelStateMap = {}
while level > 1:
    currentLevel = loadLevel(level)
    state = getLastLevelState(level)
    levelResult: ActionResult = playLevel(currentLevel, state)
    cacheLevelResults(levelResult)
