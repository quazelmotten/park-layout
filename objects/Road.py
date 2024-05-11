from ParkObject import ParkObject  # Import ParkObject from the same folder

class Road(ParkObject):
  def __init__(self, canvas, x1, y1, x2, y2):
    super().__init__(canvas, x1, y1, x2, y2, "gray", 3)  # Modify color and width as needed