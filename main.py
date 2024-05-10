import tkinter as tk
from math import sqrt

class ParkLayout:
  def __init__(self):
    self.window = tk.Tk()
    self.window.title("Park Layout")

    # Create menu frame
    self.menu_frame = tk.Frame(self.window, width=100, height=500, bg="lightgray")
    self.menu_frame.pack(side="left")

    # Create placement buttons
    self.placing_points = True  # Flag to track placement mode
    self.temp_entrance_id = None

    self.place_point_button = tk.Button(self.menu_frame, text="Place Point", command=self.set_placement_mode, bg="lightgreen")
    self.place_point_button.pack(pady=10)
    self.place_entrance_button = tk.Button(self.menu_frame, text="Place Entrance", command=self.set_placement_mode, bg="lightcoral")
    self.place_entrance_button.pack(pady=10)

    # Canvas and other initialization
    self.canvas = tk.Canvas(self.window, width=500, height=500)
    self.canvas.pack()
    self.points = []
    self.polygon_id = None
    self.entrances = []

    # Bind events
    self.canvas.bind("<Button-1>", self.handle_click)
    self.window.bind("<Return>", self.toggle_mode)
    self.canvas.bind("<Motion>", self.update_temp_entrance)  # Optional for live update

  def set_placement_mode(self):
    self.placing_points = not self.placing_points
    if self.placing_points:
      self.place_point_button.config(bg="lightgreen")
      self.place_entrance_button.config(bg="lightgray")
      self.canvas.delete(self.temp_entrance_id)  # Clear temporary entrance
      self.temp_entrance_id = None
    else:
      self.place_point_button.config(bg="lightgray")
      self.place_entrance_button.config(bg="lightcoral")

  def update_temp_entrance(self, event):
    x, y = event.x, event.y
    if self.placing_points:
      return  # Don't show temporary entrance for points
    if self.is_valid_placement(x, y):  # Check for valid placement area (e.g., only on borders)
      if self.temp_entrance_id:
        self.canvas.delete(self.temp_entrance_id)  # Clear previous temporary entrance
      self.temp_entrance_id = self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="blue", outline="blue")  # Create temporary entrance

  def handle_click(self, event):
    x, y = event.x, event.y
    if self.placing_points:
      self.add_point(x, y)
    else:
      self.check_entrance(x, y)

  def add_point(self, x, y):
    # Check if point is within existing polygon (optional)
    if self.is_within_polygon(x, y):  # Implement is_within_polygon function if needed
      return
    self.points.append((x, y))
    self.draw_polygon()

  def draw_polygon(self):
    # Clear previous polygon if any
    if self.polygon_id:
      self.canvas.delete(self.polygon_id)

    # Create polygon object with green outline and fill
    self.polygon_id = self.canvas.create_polygon(self.points, outline="green", fill="green", width=2)

  def check_entrance(self, x, y):
    if self.is_on_border(x, y):
      self.canvas.delete(self.temp_entrance_id)  # Clear temporary entrance
      self.canvas.create_oval(x-4, y-4, x+4, y+4, fill="blue")  # Create permanent entrance
      self.entrances.append((x, y))

  def is_on_border(self, x, y):
    tolerance = 10  # Adjust tolerance as needed
    for i in range(len(self.points)):
        prev_index = (i - 1) % len(self.points)
        x1, y1 = self.points[prev_index]
        x2, y2 = self.points[i]

        # Calculate distance from click point to line segment
        numerator = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1)
        denominator = sqrt((y2 - y1) ** 2 + (x2 - x1) ** 2)
        distance = numerator / denominator

        if distance <= tolerance:
            return True

    return False

  def is_valid_placement(self, x, y):  # Placeholder function, implement your logic here
    # Implement logic to check if the click is within a valid placement area for entrances
    # This could involve checking if the click is close enough to the border or within the polygon
    # You can modify this function based on your specific requirements
    pass

  def toggle_mode(self, event):
    if self.placing_points:
      self.canvas.delete("text")  # Remove instructions
      self.canvas.create_text(250, 20, text="Click on the border to place entrances", font=("Arial", 12), fill="black")
      self.canvas.create_text(250, 40, text="Press Enter to finish", font=("Arial", 12), fill="black")
      self.placing_points = False
    else:
      self.window.unbind("<Button-1>")  # Unbind click for entrances
      self.window.unbind("<Return>")   # Unbind Enter

  def is_within_polygon(self, x, y):  # Placeholder function, implement your logic here
    # Implement a function to check if a point is within the defined polygon
    # using libraries like Shapely (https://shapely.readthedocs.io/)
    # or custom point-in-polygon algorithms
    pass

  def run(self):
    self.window.mainloop()

# Create and run the ParkLayout object
park_layout = ParkLayout()
park_layout.run()