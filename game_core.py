class GameCore:

    def __init__(self):
        self.input = []


    def add_input(self):
        i=0
        while i<9:
            user_input = input()
            self.input.append(user_input)
            print(self.input)
            i+=1
