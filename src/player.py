# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

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


room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

class Player:
    def __init__(self, name, current_room, items = []):
        self.name = name
        self.current_room = current_room
        self.items = items
    
    def __str__(self):
        return f'{self.name, self.current_room, self.items}'
    
    def move_to(self, direction, current_room):
        attribute = direction.lower() + '_to'
        
        if hasattr(current_room, attribute):
            return getattr(current_room, attribute)

        print("! Nah, you can't go this way. !")
        print()

        return current_room

    def check_pockets(self):
        return f"You look inside your pockets and see :{self.items}"

    def drop_item(self, x):
        pass

    def pick_up_items(self, x):
        #check that item is in current room
        if x == 'None':
            pass
        if x in self.current_room.print_items():
            #add item to player items
            self.items.append(x)
            #delete it from room items 
            for index, item in enumerate(self.current_room.room_items):
                if str(item) == x:
                    del self.current_room.room_items[index]
                else:
                    print('it didnt work')

            #self.current_room.room_items.remove(x)
            print()
            print(f'The {x} is now in your pockets.')
            print("(to see what you have, just type 'check pockets')")
        else:
            return "It didn't work out"
