from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# getattr

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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
    def __init__(self):
        self = self
    def moveLocation(room_name, direction):
            if(direction == "n"):
                    print("You traveled North")
                    room_info.changeRoom(room_name, direction)
            elif(direction == "e"):
                    print(f"You traveled East")
                    room_info.changeRoom(room_name, direction)
            elif(direction == "s"):
                    print(f"You traveled South")
                    room_info.changeRoom(room_name, direction)
            elif(direction == "w" ):
                    print(f"You traveled West")
                    room_info.changeRoom(room_name, direction)
            else:
                    print("That doesn't lead anywhere")

user_is_playing = True
while user_is_playing == True:
    name = input("Welcome Player! Please input your name here: ") 
    name = str(name)

    player_account = Player(name, "Rugged Adventurer")
    room_info = Room()

    user_is_playing = False

    checkpoint1 = True
    while checkpoint1:
        if(player_account.p_name):
            player_account.inputName(player_account.p_name)
        else:
            print("No name entered. Try again!")
        if(len(name) < 3 or len(name) > 20):
            pass
        else: 
                print(f"{player_account.p_name} this is Room {room_info.r_name}")
                print(f"{player_account.p_name} you have {player_account.bag} in your inventory.")
                print("---------------------------")
                print(f"Room Description: {room_info.r_desc}")
                print(f"Room Items: {room_info.r_items}")
                print("---------------------------")
                player_command = input("Choose an action Move(m) or Inspect(i): ")
                player_command = str(player_command)
                print("---------------------------")
        if(player_command == "m"):
            player_direction = input("Choose a direction North(n), South(s), East(e) West(e): ")
            player_direction = str(player_direction)
            Adventure.moveLocation(room_info.r_name, player_direction)
        elif(player_command == "i"):
            print(f"The items in the room are {room_info.r_items}")
            player_action, item_name = input("Add an item by using command Take(t)/Get(g), Drop an item Drop(d), or Leave the room with Move(m) room: ").split()
            player_action = str(player_action)
            if(player_action == "t" or player_action == "g"):
                if(item_name in room_info.r_items):
                    player_account.grabItem(item_name)
                    room_info.removeItem(room_info.r_name, item_name)
                else:
                    print("That Item does not exist")
            elif(player_action == "d"):
                    player_account.bag.remove(f"{item_name}")
            elif(player_action == "m"):
                    player_direction = input("Choose a direction North(n), South(s), East(e) West(e): ")
                    player_direction = str(player_direction)
                    Adventure.moveLocation(room_info.r_name, player_direction)
            else:
                print("That is not a valid command")
        else:
            print("That is not a valid command")
checkpoint1 = True