class Room: 
    def __init__(self, room_name = "outside", room_description = "Outside Cave Entrance", room_items = ["Rock"]):
        self.r_name = room_name
        self.r_desc = room_description
        self.r_items = room_items

    def changeRoom(self, name, direction):
        if(name == "outside" and direction == "n"):
            self.r_name = "foyer"
            self.r_desc = "Dim light filters in from the south. Dusty passages run north and east."
            self.r_items = ["Fan", "Shield"]
        elif(name == "foyer" and direction == "n"):
            self.r_name = "overlook"
            self.r_desc = "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."
            self.r_items = ["Sword", "Flower"]
        elif(name == "foyer" and direction == "s"):
            self.r_name = "outside"
            self.r_desc = "Dim light filters in from the south. Dusty passages run north and east."
            self.r_items = ["Rock"]
        elif(name == "foyer" and direction == "e"):
            self.r_name = "narrow"
            self.r_desc = "The narrow passage bends here from west to north. The smell of gold permeates the air."
            self.r_items = ["Dagger", "Bandage"]
        elif(name == "overlook" and direction == "s"):
            self.r_name = "foyer"
            self.r_desc = "Dim light filters in from the south. Dusty passages run north and east."
            self.r_items = ["Fan", "Shield"]
        elif(name == "narrow" and direction == "w"):
            self.r_name = "foyer"
            self.r_desc = "Dim light filters in from the south. Dusty passages run north and east."
            self.r_items = ["Fan", "Shield"]
        elif(name == "narrow" and direction == "n"):
            self.r_name = "treasure"
            self.r_desc = "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."
            self.r_items = ["Skull", "Dust"]
        elif(name == "treasure" and direction == "n"):
            self.r_name = "narrow"
            self.r_desc = "The narrow passage bends here from west to north. The smell of gold permeates the air."
            self.r_items = ["Fan", "Shield"]
        else:
            print("This is a deadend.")
        
    def removeItem(self, room, item_name):
            self.r_items.remove(f"{item_name}")
            