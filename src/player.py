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
    def __init__(self, name, roomname, room_des, items = []):
        self.name = name
        self.roomname = roomname
        self.room_des = room_des
        self.items = items
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    #Lesson code

    def move_to(direction, roomname):
        #move in specified direction
        attribute = direction + '_to' #to match above

        print(room[roomname])
        
        if hasattr(room[roomname], attribute): # won't let us move w/o attribute of room 
            return getattr(room[roomname], attribute) #gets the room we are moving to
        else:
            print('cant move here')

        return roomname
