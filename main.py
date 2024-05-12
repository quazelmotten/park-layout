import tkinter as tk
from ParkObject import ParkObject  # Import ParkObject from the objects folder
from objects.Road import Road  # Import Road from the objects folder
from objects.Border import Border
from objects.Entrance import Entrance

class ParkLayout:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Park Layout")

        self.current_object = None  # Initially no object selected
        self.current_border = None  # Initially no border object being created

        # Create menu frame
        self.menu_frame = tk.Frame(self.window, width=100, height=500, bg="lightgray")
        self.menu_frame.pack(side="left")

        # Load button icons
        self.road_icon = self.create_image("road.png")
        self.border_icon = self.create_image("border.png")
        self.entrance_icon = self.create_image("entrance.png")

        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.bind("<Button-1>", self.handle_click_on_canvas)
        self.canvas.pack()

        # Create buttons (with icons)
        self.current_object = "border"
        self.road_button = tk.Button(self.menu_frame, text="Road", image=self.road_icon, compound=tk.LEFT, command=lambda: self.set_object("road"), bg="lightgray")
        self.road_button.pack(pady=10)
        self.border_button = tk.Button(self.menu_frame, text="Border", image=self.border_icon, compound=tk.LEFT, command=lambda: self.set_object("border"), bg="lightgray")
        self.border_button.pack(pady=10)
        self.entrance_button = tk.Button(self.menu_frame, text="Entrance", image=self.entrance_icon, compound=tk.LEFT, command=lambda: self.set_object("entrance"), bg="lightgray")
        self.entrance_button.pack(pady=10)
          # Create buttons with proper event binding
        self.road_button.bind("<Button-1>", self.set_object("road"))
        self.border_button.bind("<Button-1>", self.set_object("border"))
        self.entrance_button.bind("<Button-1>", self.set_object("entrance"))

        # Canvas and other initialization

        self.objects = []  # List to store all park objects

        # Bind events


    def create_image(self, filename):
    # Implement logic to create a square image from a file (considering size)
    # You can use libraries like PIL (Pillow) for image manipulation
    # This function should return a PhotoImage object suitable for the button
        from PIL import Image, ImageTk  # Assuming you have PIL installed
        image = Image.open(filename).resize((20, 20), Image.ANTIALIAS)  # Resize image to 20x20 pixels
        return ImageTk.PhotoImage(image)

    def set_object(self, text):
        # Get the button that was clicked

        # Get the text of the clicked button (lowercase for consistency)
        clicked_object = text

        # Update current_object based on the clicked button text
        if clicked_object == "road":
            self.current_object = "road"
        elif clicked_object == "border":
            self.current_object = "border"
            self.current_border = Border(self.canvas)
        elif clicked_object == "entrance":
            self.current_object = "entrance"
        else:
            # Handle unexpected button text (optional)
            print(f"Unknown object type: {clicked_object}")
        print(self.current_object)

    def handle_click_on_canvas(self, event):
  # Check if current object is "border"
        if self.current_object == "border":
            # Get the click coordinates
            x = event.x
            y = event.y

            # If current_border exists, add the point to it
            if self.current_border:
                self.current_border.add_point(x, y)
            print(x,y)

# Additional code to handle finalizing the border (optional)
    def finalize_border(self):
        if self.current_border:
            if self.current_border.finalize():  # Call finalize on the current border object
                self.current_border = None  # Clear current border object (since finalized)

    def run(self):
        self.window.mainloop()

# Create and run the ParkLayout object
park_layout = ParkLayout()
park_layout.run()