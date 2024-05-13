from objects.Border import Border

class ProhibitedZone(Border):
  def __init__(self, canvas, color="#FF0000"):  # Red color by default
    super().__init__(canvas, color)

  def draw(self):
    """
    Draws the prohibited zone using the specified color.
    """
    points = self.points
    self.canvas.create_polygon(points, fill=self.color, outline=self.color)
