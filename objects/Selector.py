class Selector():
    def __init__(self):
        self.t = 1
        self.selected_object = None

    def print_object(self, event, current_object, canvas):
        if self.selected_object:
            canvas.itemconfig(self.selected_object.id, fill=self.selected_object.color)
        self.selected_object = current_object
        print(f"Current object:{self.selected_object}") 
        canvas.itemconfig(current_object.id, fill='red')
        return
    