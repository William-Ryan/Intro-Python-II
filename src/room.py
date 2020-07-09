class Room(): 
    def __init__(self, name, description):
        self.r_name = name
        self.r_desc = description
    
    def whichRoom(self, room_name, direction):
        if(room_name == "Outside"):
            self.r_name = room_name
            print(f"this room's name is {self.r_name}")
            self.r_desc = "Outside Cave Entrance. North of you, the cave mount beckons"
            print(f"Room Description {self.r_desc}")
            if(direction == "n"):
                self.r_name == "Foyer"
                self.r_desc = "Dim light filters in from the south. Dusty passages run north and east."
            else:
                print("That leads nowhere.")
        else:
            print("This room does not exist")

            