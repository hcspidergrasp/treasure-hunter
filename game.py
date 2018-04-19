from utils.levels import LevelCodes
from utils.parser import LevelParser

LEVEL_CODES_FILE_PATH = "assets/levels.dat"
START_LEVEL_CODE = 100

levelCodes = LevelCodes(LEVEL_CODES_FILE_PATH)

levelParser = LevelParser()
levelParser.parseLevel(levelCodes.resolveLevelFileByCode(START_LEVEL_CODE))

currentLevel = levelParser.parsedLevel
