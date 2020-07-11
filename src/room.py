class Room: 
    def __init__(self, room_name = "outside", room_description = "Outside Cave Entrance"):
        self.r_name = room_name
        self.r_desc = room_description

    def changeRoom(self, name, direction):
        if(name == "outside" and direction == "n"):
            self.r_name = "foyer"
            self.r_desc = "Dim light filters in from the south. Dusty passages run north and east."
        elif(name == "foyer" and direction == "n"):
            self.r_name = "overlook"
            self.r_desc = "A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm."
        elif(name == "foyer" and direction == "s"):
            self.r_name = "outside"
            self.r_desc = "Dim light filters in from the south. Dusty passages run north and east."
        elif(name == "foyer" and direction == "e"):
            self.r_name = "narrow"
            self.r_desc = "The narrow passage bends here from west to north. The smell of gold permeates the air."
        elif(name == "overlook" and direction == "s"):
            self.r_name = "foyer"
            self.r_desc = "Dim light filters in from the south. Dusty passages run north and east."
        elif(name == "narrow" and direction == "w"):
            self.r_name = "foyer"
            self.r_desc = "Dim light filters in from the south. Dusty passages run north and east."
        elif(name == "narrow" and direction == "n"):
            self.r_name = "treasure"
            self.r_desc = "You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."
        elif(name == "treasure" and direction == "n"):
            self.r_name = "narrow"
            self.r_desc = "The narrow passage bends here from west to north. The smell of gold permeates the air."
        else:
            print("This is a deadend.")