from ParkObject import ParkObject

class Border(ParkObject):
  def __init__(self, canvas):
    super().__init__(canvas, None, None, None, None, "black", 2)  # No initial points for border
    self.canvas = canvas
    self.points = []  # List to store border points
    self.id = None  # Id of the border polygon

  def add_point(self, x, y):
    self.points.append((x, y))
    if self.id:  # If a border polygon exists, update it with the new point
      self.canvas.delete(self.id)  # Clear existing polygon
      self.id = self.canvas.create_polygon(self.points, close=True, outline="black", fill="none", width=2)  # Create updated polygon

