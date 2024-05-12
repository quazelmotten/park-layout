from ParkObject import ParkObject

class Border(ParkObject):
  def __init__(self, canvas):
    self.canvas = canvas
    self.points = []  # List to store border points
    self.id = None  # Id of the border polygon

    # Bind click handler to the canvas
    self.canvas.bind("<Button-1>", self.handle_click)

  def add_point(self, x, y):
    self.points.append((x, y))
    if self.id:  # If a border polygon exists, update it with the new point
      self.canvas.delete(self.id)  # Clear existing polygon
      self.id = self.canvas.create_polygon(self.points, close=True, outline="black", fill="none", width=2)  # Create updated polygon

  def handle_click(self, event):
    # Get the click coordinates
    x = event.x
    y = event.y

    # Add the click coordinates to the border points list
    self.add_point(x, y)