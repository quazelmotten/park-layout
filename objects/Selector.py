class Selector():
    def __init__(self):
        self.t = 1
    def print_object(self, event, current_object):
        self.current_object = current_object
        print(f"Current object:{self.current_object}") 
        return