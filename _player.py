class Player:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.inv = {}
        self.maxHealth = 100
        self.health = self.maxHealth

    def moveEast(self):
        self.x += 1

    def moveWest(self):
        self.x -= 1

    def moveNorth(self):
        self.y += 1

    def moveSouth(self):
        self.y -= 1

    def addCoins(self, count=1):
        self.coins += count

    def removeCoins(self, count=1):
        if not (self.coins - count < 0):
            self.coins -= count
        else:
            raise Exception("Coins cannot drop below 0")

    def addHealth(self, count=1):
        if (self.health + count <= self.maxHealth):
            self.health += count
        else:
            self.health = self.maxHp

    def removeHealth(self, count=1):
        if (self.health - count > 0):
            self.health -= count
        else:
            raise Exception("HP cannot fall below 0 - you are dead.")

    def addItemToInv(self, item, quantity=1):
        if item not in self.inv.keys():
            self.inv[item] = quantity
        else:
            self.inv[item] += quantity;

    def removeItemFromInv(self, item, quantity=1):
        if item in self.inv[item]:
            self.inv[item] = quantity
        else:
            raise Exception("Cannot remove a non-existant item")


    def viewInv(self):
        # Assemble list of formatted displayable items
        displayableItems = []

        for item in self.inv.keys():
            if (self.inv[item] > 0 and (self.inv[item] != 1)):
                displayableItems.append(f">>> {item.name} - {self.inv[item]}")
            elif (self.inv[item] == 1):
                displayableItems.append(f">>> {item.name}")

        print("--- Inventory ---")
        if len(displayableItems) > 0:
            for line in displayableItems:
                print(line)
        else:
            print("> No items")
        print("")

    def viewCoords(self):
        print("--- Co-ords ---")
        print(f"({self.x},{self.y})")
        print("")

    def getCoins(self):
        return self.inv["coins"]
