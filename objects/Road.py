from ParkObject import ParkObject

class Road(ParkObject):
  def __init__(self, canvas, start_x, start_y, end_x, end_y, width=5, color="#000000"): # Call the ParkObject constructor
    self.canvas = canvas
    self.points = [(start_x, start_y), (end_x, end_y)]  # List of start and end points for the road line
    self.id = None  # Id of the line object on the canvas
    self.width = width
    self.color = color

    self.create_road()  # Create the road line on the canvas

  def create_road(self):
    self.id = self.canvas.create_line(self.points[0][0], self.points[0][1], self.points[1][0], self.points[1][1], width=self.width, fill=self.color)  # Create line object

  def update_end_point(self, new_x, new_y):
    self.points[1] = (new_x, new_y)  # Update the end point of the road line
    self.canvas.delete(self.id)  # Delete the old line
    self.create_road()  # Recreate the line with the updated end point

  # Implement other methods as needed (e.g., setting color, width)