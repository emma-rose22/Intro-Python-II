# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, roomname, description, items = []):
        self.roomname = roomname
        self.description = description
        self.items = items

    def __str__(self):
        return f"{self.roomname}"

    def print_description(self):
        return f"{self.description}"

    def print_items(self):
        return f"{self.items}"