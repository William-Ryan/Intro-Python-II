from room import Room

# # Declare all the rooms

# room = {
#     'outside':  Room("Outside Cave Entrance",
#                      "North of you, the cave mount beckons"),

#     'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east."""),

#     'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm."""),

#     'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air."""),

#     'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south."""),
# }


# # Link rooms together

# room['outside'].n_to = room['foyer']
# room['foyer'].s_to = room['outside']
# room['foyer'].n_to = room['overlook']
# room['foyer'].e_to = room['narrow']
# room['overlook'].s_to = room['foyer']
# room['narrow'].w_to = room['foyer']
# room['narrow'].n_to = room['treasure']
# room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
class Adventure():
    def __init__(self, player_name, current_room = "Outside", current_description = "Outside Cave Entrance"):
        self.p_name = player_name
        self.c_room = current_room
        self.c_description = current_description
    
    def inputName(self, name):
        if(len(name) < 3 or len(name) > 20):
            print("Invalid Name. Name must be between 3 and 20 letters. Try Again!")
        else:
            self.p_name = name
            return self.p_name
    
    def moveLocation(self, direction):
        if(direction == "n"):
            print(f"You traveled North")
        elif(direction == "e"):
            print(f"You traveled East")
        elif(direction == "s"):
            print(f"You traveled South")
        elif(direction == "w" ):
            print(f"You traveled West")
        else:
            print("That doesn't lead anywhere")


name = input("Welcome Player! Please input your name here: ") 
name = str(name)

player_account = Adventure(name)

# print(player_account.p_name)

if(player_account.p_name):
    player_account.inputName(player_account.p_name)
    if(len(name) < 3 or len(name) > 20):
        pass
    else:
        print("---------------------------")
        print(f"Congratulations {player_account.p_name}! Enjoy the game!")
        print("---------------------------")
        print("---------------------------") 
        print(f"{player_account.p_name} this is Room {player_account.r_name}")
        print("---------------------------")
        print(f"Room Description: {player_account.r_description}")
        print("---------------------------")
        location = input("Choose a direction North[n], South[s], East[e], West[w]: ")
        location = str(location)
        print("---------------------------")
        player_account.moveLocation(location)
        
else:
    print("No name entered. Try again!")

