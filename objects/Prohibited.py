from objects.Border import Border

class ProhibitedZone(Border):
  def __init__(self, canvas):  # Red color by default
    super().__init__(canvas)
    self.color = "#D3D3D3"

  def add_point(self, x, y):
      self.points.append((x, y))
      self.canvas.delete(self.id)
      self.id = self.canvas.create_polygon(self.points, outline="#004D40", fill=self.color, width=2)
