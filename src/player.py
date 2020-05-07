# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, roomname, room_des, items = []):
        self.name = name
        self.roomname = roomname
        self.room_des = room_des
        self.items = items