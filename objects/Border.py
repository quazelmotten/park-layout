from ParkObject import ParkObject

class Border(ParkObject):
  def __init__(self, canvas, points = []):
    self.canvas = canvas
    self.entrances = []
    self.points = points # List to store border points
    self.id = None  # Id of the border polygon
    self.color = "#80CBC4"
    if self.points:
      self.canvas.create_polygon(self.points, outline="#004D40", fill=self.color, width=2)

  def add_point(self, x, y):
    self.points.append((x, y))
    self.canvas.delete(self.id)
    self.id = self.canvas.create_polygon(self.points, outline="#004D40", fill=self.color, width=2)  # Create updated polygon

  def handle_click(self, event):
    # This function won't be called directly anymore (event handling managed elsewhere)
    pass  # Placeholder

  def finalize(self):
    # Implement logic to mark the border as finalized (optional)
    # This could involve changing a flag or performing final calculations
    return True