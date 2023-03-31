from _player import Player
from _items import Weapon
from _items import Item
from _rooms import Room
from _rooms import RoomWithItems

rooms = []
rooms.append(RoomWithItems(0, 0, "You stand looking into the mouth of a cave", "A cold breeze rushes from the cave as you peer into the darkness", {"n":True, "s":False, "e":False, "w":False}))
rooms.append(RoomWithItems(0, 1, "You are standing in the cave", "The walls are wet and cold, there is a door to the east", {"n":False, "s":True, "e":False, "w":True}, items=[Item("Key", "A small brass key", "sits on the floor")]))
rooms.append(RoomWithItems(-1, 1, "You are standing in a small room.", "There is a wooden chest directly ahead of you. It looks very old.", {"n":False, "s":False, "e":True, "w":False}))

p = Player()

starterKit = [
    [Weapon(name="Sword", description="A short steel sword with ornate elvish carvings on the hilt", damagePoints=3), 1],
    [Item(name="Rope", description="A 20 meter length of rope"), 20],
    [Item(name="Candle", description="A candlestick made of strange smelling yellow wax"), 6],
    [Item(name="Dynamite", description="Loose dirty-red sticks in a metal box"), 2],
    [Item(name="Coins", description="A variety of coins in a small leather bag"), 2]
]

cannotGoMessage = "You cannot go that way";

for x in starterKit:
    p.addItemToInv(x[0], x[1])

def getCurrentRoom(x, y):
    for room in rooms:
        if room.x == x and room.y == y:
            return room

    raise Exception(f"Out of bounds ({x}, {y})")

def handleCommand(com):
    com = com.lower()
    if "north" in com:
        if currentRoom.canGo["n"]:
            p.moveNorth()
        else:
            print(cannotGoMessage)
    elif "south" in com:
        if currentRoom.canGo["s"]:
            p.moveSouth()
        else:
            print(cannotGoMessage)
    elif "east" in com:
        if currentRoom.canGo["e"]:
            p.moveEast()
        else:
            print(cannotGoMessage)
    elif "west" in com:
        if currentRoom.canGo["w"]:
            p.moveWest()
        else:
            print(cannotGoMessage)
    elif "check" in com:
        if isinstance(currentRoom, RoomWithItems):
            print(currentRoom.viewItems())
        else:
            print("There are no objects in this room")
    elif "pick" in com or "get" in com or "take" in com:
        if isinstance(currentRoom, RoomWithItems):
            for item in currentRoom.items:
                if item.name.lower() in com:
                    p.addItemToInv(item)
                    currentRoom.removeItem(item)
                    print(f"You pick up the {item.name} and add it to your bag")
    elif "show" in com:
        if "bag" in com or "inventory" in com:
            p.viewInv()
        if "coords" in com or "location" in com:
            p.viewCoords()
    elif "look" in com:
        currentRoom.viewLongDescription()
    else:
        print("Unknown Command")

gameloop = True
while gameloop:
    print("\n")
    currentRoom = getCurrentRoom(p.x, p.y)
    print(currentRoom.description)
    com = input("> ")
    handleCommand(com)
