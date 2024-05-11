import tkinter as tk
from ParkObject import ParkObject  # Import ParkObject from the objects folder
from objects.Road import Road  # Import Road from the objects folder
from objects.Border import Border
from objects.Entrance import Entrance

class ParkLayout:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Park Layout")

        # Create menu frame
        self.menu_frame = tk.Frame(self.window, width=100, height=500, bg="lightgray")
        self.menu_frame.pack(side="left")

        # Load button icons
        self.road_icon = self.create_image("road.png")
        self.border_icon = self.create_image("border.png")
        self.entrance_icon = self.create_image("entrance.png")

        # Create buttons (with icons)
        self.current_object = "border"
        self.road_button = tk.Button(self.menu_frame, text="Road", image=self.road_icon, compound=tk.LEFT, command=self.set_object, bg="lightgray")
        self.road_button.pack(pady=10)
        self.border_button = tk.Button(self.menu_frame, text="Border", image=self.border_icon, compound=tk.LEFT, command=self.set_object, bg="lightgray")
        self.border_button.pack(pady=10)
        self.entrance_button = tk.Button(self.menu_frame, text="Entrance", image=self.entrance_icon, compound=tk.LEFT, command=self.set_object, bg="lightgray")
        self.entrance_button.pack(pady=10)

        # Canvas and other initialization
        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.pack()
        self.objects = []  # List to store all park objects

        # Bind events
        self.canvas.bind("<Button-1>", self.handle_click)

    def create_image(self, filename):
    # Implement logic to create a square image from a file (considering size)
    # You can use libraries like PIL (Pillow) for image manipulation
    # This function should return a PhotoImage object suitable for the button
        from PIL import Image, ImageTk  # Assuming you have PIL installed
        image = Image.open(filename).resize((20, 20), Image.ANTIALIAS)  # Resize image to 20x20 pixels
        return ImageTk.PhotoImage(image)

    def set_object(self):
        self.current_object = self.road_button.cget("text").lower()  # Get the text of the clicked button

    def handle_click(self, event):
        x, y = event.x, event.y
        if self.current_object == "road":
            self.objects.append(Road(self.canvas, x-10, y, x+10, y))  # Adjust line length as needed
        elif self.current_object == "border":
              # Check if no border object is currently being created
            self.current_border = Border(self.canvas)  # Create a new Border object
            self.objects.append(self.current_border)  # Add the border object to the list of objects
            self.current_border.add_point(x, y)  # Add clicked point to  the border object
        elif self.current_object == "entrance":
            self.objects.append(Entrance(self.canvas, x, y))

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