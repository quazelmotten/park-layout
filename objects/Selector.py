class Selector():
    def __init__(self):
        self.t = 1
        self.selected_object = None

    def print_object(self, current_object):
        self.selected_object = current_object
        print(f"Current object:{self.selected_object}") 
        return