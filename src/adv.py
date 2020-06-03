from room import Room
from player import Player
from item import Item

#make some item objects
item ={
    'potato' : Item('potato', 'average size potato'),
    'big potato' : Item('big potato', 'an impressively large potato')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [item['big potato']]),

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

print('Welcome to the game, adventurer! What is your name?')

player_name = input()

player = Player(player_name, room['outside'], [item['potato'].i_name])

print(player)

while True:

    print(f'---: {player.current_room} :---')
    print('_______________________________________________')
    print(f'* {player.current_room.description} *')
    print('_______________________________________________')
    print()

    #share if items are in room, give option to add them to pockets
    if player.current_room.print_items() == None:
        print(f'The {player.current_room} is empty of any valuables.')
        #print(f'player pockets', player.check_pockets())
    else:
        print(f'There is some stuff in the {player.current_room}:')
        print(player.current_room.print_items())
        print('Type in what you want to pick up, or just say None.')
        p_input = input('~~~>')
        player.pick_up_items(p_input)

    print()
    print(f'Which direction do you want to go, {player_name}?')
    p_input = input('~~~>')
    print()
    print()
    print()
    print()
    print()
    print()

    if p_input == 'exit':
        print(f'Come back soon {player_name}!')
        break
    if p_input == 'check pockets':
        print(player.check_pockets())
        print()
    
    if p_input == 'drop item':
        drop_item = print('Please type the item you want to drop')
        drop_item = input('~~~>')
        print(player.drop_item(drop_item))

    #move rooms
    else:
     player.current_room = player.move_to(p_input, player.current_room)
