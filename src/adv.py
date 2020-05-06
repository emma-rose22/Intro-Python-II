from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

def item_verbs(x, y = None):
    '''Gives player the ability to pick up and drop items'''
    if x == 'take':
        player_1.items.append(y)
        room.item_list.remove(y)
        print(f'{y} successfully added to your inventory!')
        print(' ')
    elif x == 'drop':
        try:
            player_1.items.remove(y)
            room.item_list.append(y)
        except:
            print("You can't drop an item that isn't in your inventory.")
    else:
        print('The item could not be added.')

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

print('Welcome to the game! What is your name, adventurer? ')
gamer_name = input()
player_1 = Player(gamer_name, 'outside') # I want to change this to user input later


print(room[player_1.roomname])
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

while True:

    print(' ')
    print(f"Current Room: {room[player_1.roomname]}")
    print(f"Room Description: {room[player_1.roomname]}")
    if room[player_1.roomname].item_list !=[]:
        while True:
            for i in room[player_1.roomname].item_list:
                print(f"Hey! there is {i} in this room.")
                print(' ')

            pickup = input(f"Do you want to pick anything up? (Hint: type 'take' and then the item name to add it to you inventory)")
            if pickup == 'no':
                print('Okay, this item will be left here.')
                print(' ')
                break
            elif pickup != 'no':
                item_verbs(pickup.split())
                break
            else:
                print("The item wasn't able to be added, please try again and make sure it is spelled correctly.")


    print(' ')

    player_input = input(f'Where do you want to go, {player_1.name}? Please print the first letter of the cardinal direction you seek: ')

    if player_input == 'exit':
        print(' ')
        print(f'Sad to see you go, {player_1.name}. Come back soon!')
        break

    try:
        if player_input == 'n':
            print('North it is! Onward, into the unknown...')
            print(' ')
            if player_1.roomname == 'outside':
                player_1.roomname = 'foyer'
                
            elif player_1.roomname == 'foyer':
                player_1.roomname = 'overlook'

            elif player_1.roomname == 'narrow':
                player_1.roomname = 'treasure'
            else:
                print('There is no passage this way... you doing okay goodman?')

        elif player_input == 's':
            print('South it is! Onward, into the unknown...')
            print(' ')
            if player_1.roomname == 'foyer':
                player_1.roomname = 'outside'

            elif player_1.roomname == 'overlook':
                player_1.roomname = 'foyer'

            elif player_1.roomname == 'treasure':
                player_1.roomname = 'narrow'

            else:
                print('There is no passage this way... you doing okay goodman?')

        elif player_input == 'e':
            print('East it is! Onward, into the unknown...')
            print(' ')
            if player_1.roomname == 'foyer':
                player_1.roomname = 'narrow'

            else:
                print('There is no passage this way... you doing okay goodman?')

        elif player_input == 'w':
            print('West it is! Onward, into the unknown...')
            print(' ')
            if player_1.roomname == 'narrow':
                player_1.roomname = 'foyer'
            else:
                print('There is no passage this way... you doing okay goodman?')
        else:
            print('Please type the first letter of the direction you would like to go.')
            print(' ')
    except:
        pass