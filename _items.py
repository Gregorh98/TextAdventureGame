class Item():
    def __init__(self, name, description, positionalDescriptionModifier = ""):
        self.name = name
        self.description = description
        self.positionalDescriptionModifier = positionalDescriptionModifier

    def viewDescription(self):
        print(self.description)

    def viewLongDescription(self):
        print(self.description, self.positionalDescriptionModifier)


class Weapon(Item):
    def __init__(self, name, description, damagePoints, maxDurability = 100, randomiseDurability = False, positionalDescriptionModifier = ""):
        super().__init__(name, description, positionalDescriptionModifier)
        self.damagePoints = damagePoints

        if randomiseDurability:
            self.durability = random.choice(range(maxDurability))
        else:
            self.durability = maxDurability