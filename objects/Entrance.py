from shapely.geometry import Polygon, Point, LineString
from ParkObject import ParkObject

class Entrance:
  def __init__(self, canvas, border, x, y, position=None):
    self.canvas = canvas
    self.border = border
    self.position = position  # Can be set to specific coordinates or None for click-based placement

    self.entrance_id = canvas.create_line(
        x, y,
        x+10, y+10,
        width=10, fill="black"
    )

    if border and border.points:  # Check for border and points
      border_points = []
      for i in border.points:
        border_points.append(i)
      self.border_polygon = Polygon(border_points)  # Create Shapely polygon

#   def calculate_entrance_point(self, click_point):
#     """
#     Calculates the entrance point directly below the click point on the border.

#     Args:
#         click_point: A tuple (x, y) representing the click coordinates.

#     Returns:
#         A tuple (x, y) representing the entrance position on the border,
#         or None if no valid intersection is found below the click.
#     """
#     if not self.border_polygon:
#       return None  # No polygon to calculate with

#     click_line = LineString([click_point, (click_point[0], float("inf"))])
#     intersections = click_line.intersection(self.border_polygon)

#     entrance_point = None
#     for point in intersections.coords:
#       if point[1] > click_point[1]:  # Check if Y-coordinate is below the click
#         entrance_point = point
#         break

#     return entrance_point

#   def create_entrance(self, click_point, canvas):
#     """
#     Creates the entrance and sets its position based on the click point or pre-defined position.

#     Args:
#         click_point: A tuple (x, y) representing the click coordinates (if position is None).
#         canvas: The Tkinter canvas object where the entrance will be drawn.
#     """
#     if not self.position:  # Use click point if position is not set
#       entrance_point = self.calculate_entrance_point(click_point)
#       if entrance_point:
#         self.position = entrance_point
#       else:
#         print("Click is not on the border or there's no intersection point below")
#         return

#     # Get the direction vector of the border segment at the entrance point
#     offset_vector = None
#     for i in range(len(self.border.points) - 2):
#       if self.border.points[i] == self.position[0] and self.border.points[i + 1] == self.position[1]:
#         # Found the border segment where the entrance is
#         prev_point = (self.border.points[i - 2], self.border.points[i - 1])
#         next_point = (self.border.points[i + 2], self.border.points[i + 3])
#         offset_vector = (next_point[0] - prev_point[0], next_point[1] - prev_point[1])
#         break

#     # Create entrance line with offset based on direction vector (assuming offset of 5 pixels on each side)
#     offset_x = offset_vector[0] / 2 if offset_vector else 0  # Handle cases with no offset vector
#     offset_y = offset_vector[1] / 2 if offset_vector else 0
#     entrance_line_coords = [
#         (self.position[0] - offset_x, self.position[1] - offset_y),
#         (self.position[0] + offset_x, self.position[1] + offset_y)
#     ]

#     # Draw the entrance line on the canvas with a width of 10 and black color
#     self.entrance_id = canvas.create_line(
#         entrance_line_coords[0][0], entrance_line_coords[0][1],
#         entrance_line_coords[1][0], entrance_line_coords[1][1],
#         width=10, fill="black"
#     )
#     print(f"Entrance created on the border at {self.position}")
