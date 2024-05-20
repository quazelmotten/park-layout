from ParkObject import ParkObject
from math import sqrt, dist

class Entrance(ParkObject):
  def __init__(self, canvas, border, x, y):
    self.canvas = canvas
    self.border = border
    self.id = None
    self.x = x
    self.y = y 
    self.color = "orange"
    self.points = [(x,y)] # Reference to the Border object
    if self.is_point_within_range((x,y), border.points) != False:
      self.position = self.is_point_within_range((x,y), border.points)
      self.draw()
    else:
      print(f"The point {x,y} is not within 10 units of the shape's edges.")
  
  def is_point_within_range(self, point, poly):
      for i in range(len(poly)):
        a, b = poly[i - 1], poly[i]
        if abs(dist(a, point) + dist(b, point) - dist(a, b)) < 15:
          print('Less than 15')
          print(a,b)
          self.sinL = abs(b[1]-a[1]) / abs(b[0]-a[0])
          return self.calculate_point(a,b, point)
      return False

  def calculate_point(self, p1, p2, p3):
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    dx, dy = x2 - x1, y2 - y1
    det = dx*dx + dy*dy
    a = (dy * (y3 - y1) + dx * (x3 - x1))/det
    return x1 + a * dx, y1 + a * dy
  
  # def calculate_sin():
     
  
  
  def draw(self):
    """
    Draws the entrance as a short black line on the canvas.
    You can customize the appearance here (e.g., line width, color).
    """
    if self.position:
      x, y = self.position
      # self.canvas.create_line(x - 5, y, 5+x*self.sinL, y*sqrt(1-self.sinL**2), fill="orange", width=2)  # Short black line
      self.id = self.canvas.create_line(x - 5, y, 5+x, y, fill="orange", width=2)