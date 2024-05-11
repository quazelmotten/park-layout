from ParkObject import ParkObject  # Import ParkObject from the same folder

class Entrance(ParkObject):
  def __init__(self, canvas, x, y):
    super().__init__(self.canvas, x-5, y-5, x+5, y+5, "blue", 2)  # Modify size and color as needed