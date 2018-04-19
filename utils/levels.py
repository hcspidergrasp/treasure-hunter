class LevelCodes:
    
    __parsedLevelCodes = None

    def __init__(self, path):
        fileIO = open(path)
        rawLevelCodes = fileIO.readlines()
        self.__parsedLevelCodes = dict()
        for line in rawLevelCodes:
            parsed = line.strip().split(" ")
            self.__parsedLevelCodes[int(parsed[0])] = parsed[1]
        fileIO.close()
        

    def resolveLevelFileByCode(self, code):
        return self.__parsedLevelCodes[code]
