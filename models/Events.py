class Events:

    def __init__(self):
        # Prison
        self.metGopnik = False
        self.keyFound = False
        self.gopnikKilled = False
        self.robedGopnik = False
        self.returnedMoney = False

        # Guardian Room
        self.metGuardian = False
        self.guardianKilled = False
        self.robedGuardian = False
        
        # Yard
        self.tauntedPigeons = False
        self.fedPigeons = False
        
        # Dragon Room
        self.metDragon = False
        self.wonDragon = False
        self.loseToDragon = False
