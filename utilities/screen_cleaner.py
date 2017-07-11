from os import system, name

class clear():

    def __init__(self):

        system('cls' if name == 'nt' else 'clear')
