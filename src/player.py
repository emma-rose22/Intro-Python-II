# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, items = ['potato']):
        self.name = name
        self.current_room = current_room
        self.items = items
    
    def move_to(self, direction, current_room):
        attribute = direction.lower() + '_to'
        
        if hasattr(current_room, attribute):
            return getattr(current_room, attribute)

        print("! You run smack into a wall. Rubbing your head, you realize you can't go this way. !")
        print()

        return current_room

    def check_pockets(self):
        return f"{self.items}"

    def pick_up_items(self, x):
        #check that item is in current room
        for i in x:
            if i in self.current_room.print_items():
                #add item to player items
                self.items.append(i)
                #delete it from room items 
                self.current_room.items.pop(i)
            else:
                return "It didn't work out"