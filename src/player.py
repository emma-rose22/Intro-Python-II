# Write a class to hold player information, e.g. what room they are in
# currently.

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

    def drop_item(self, x):
        #add to current room
        if x in self.items:
            self.current_room.room_items.append(x)
            #remove from pockets
            for index, item in enumerate(self.items):
                if str(item) == x:
                    del self.items[index]
                else:
                    print('drop didnt work')

    def pick_up_items(self, x):
        #check that item is in current room
        if x == 'None':
            pass
        if x in self.current_room.print_items():
            #add item to player items
            self.items.append(x)
            #delete it from room items 
            for index, item in enumerate(self.current_room.print_items()):
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
