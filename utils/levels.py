class LevelCodes:

    def __init__(self, path):
        rawLevelCodes = open(path).readlines()
        self._parsedLevelCodes = dict()
        for line in rawLevelCodes:
            parsed = line.strip().split(" ")
            self._parsedLevelCodes[parsed[0]] = parsed[1]
        

    def resolveLevelFileByCode(self, code):
        return self._parsedLevelCodes[code]
