class Item:

    def __init__(self, i_name, i_description):
        self.i_name = i_name
        self.i_description = i_description

    def __str__(self):
        return f'{self.i_name}'#: {self.i_description}'