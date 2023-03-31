class Room():
    def __init__(self, x, y, description, longDescription, canGo={"n":True, "s":True, "e":True, "w":True}):
        self.x = x
        self.y = y
        self.description = description
        self.longDescription = longDescription
        self.canGo = canGo

    def viewDescription(self):
        print(self.description)

    def viewLongDescription(self):
        print(self.longDescription)


class RoomWithItems(Room):
    def __init__(self, x, y, description, longDescription, canGo, items=[]):
        super().__init__(x, y, description, longDescription, canGo)
        self.items = items

    def viewItems(self):
        for item in self.items:
            print(f">>> {item.name} - {item.description}")

    def viewLongDescription(self):
        print(self.longDescription)
        for item in self.items:
            item.viewLongDescription()

    def addItem(self, item):
        self.items.append(item)

    def removeItem(self, item):
        self.items.pop(self.items.index(item))
