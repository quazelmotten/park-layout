class ParkObject:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = None  # No object created by default
        self.x = None
        self.y = None
    def get_id(self):
      return self.id