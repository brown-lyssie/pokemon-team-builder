class Pokemon():
    # constructor
    speciesID = None
    heldItemID = None
    abilityID = None
    moveIDs = [None] * 4 # 4-long array of Nones
    level = None
    def __init__(self):
        print("initializing a Pokemon")
        #print(self)
    def __str__(self):
        string = "Pokemon with "
        string += "species ID: " + str(self.speciesID) + ", "
        string += "Held item ID: " + str(self.heldItemID) + ", "
        string += "Ability ID: " + str(self.abilityID) + ", "
        string += "Move IDs: " + str(self.moveIDs) + ", "
        string += "Level: " + str(self.level)
        return string