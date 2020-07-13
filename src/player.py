class Player:
    def __init__(self, player_name, player_description, inventory = ["Journal"]):
        self.p_name = player_name
        self.p_desc = player_description
        self.bag = inventory

        
    def grabItem(self, item_name):
        if(item_name == None):
            print("This item does not exist (At least in this room).")
        else:
            self.bag.append(item_name)
            return self.bag