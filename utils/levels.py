class LevelCodes:
    __parsedLevelCodes = None

    def __init__(self, path):
        file_io = open(path)
        raw_level_codes = file_io.readlines()
        self.__parsedLevelCodes = dict()
        for line in raw_level_codes:
            parsed = line.strip().split(" ")
            self.__parsedLevelCodes[int(parsed[0])] = parsed[1]
        file_io.close()

    def resolve_level_file_by_code(self, code):
        return self.__parsedLevelCodes[code]
