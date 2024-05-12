class ParkObject:
    def __init__(self, canvas):
        self.canvas = canvas
        self.id = None  # No object created by default

    def get_id(self):
      return self.id