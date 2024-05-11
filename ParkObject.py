class ParkObject:
  def __init__(self, canvas, x1, y1, x2, y2, color, width):
    self.canvas = canvas
    self.id = self.canvas.create_line(x1, y1, x2, y2, fill=color, width=width)

  def get_id(self):
    return self.id