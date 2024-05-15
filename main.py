import tkinter as tk
from ParkObject import ParkObject  # Import ParkObject from the objects folder
from objects.Road import Road  # Import Road from the objects folder
from objects.Border import Border
from objects.Entrance import Entrance
from objects.Prohibited import ProhibitedZone
from objects.Selector import Selector

class ParkLayout:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Park Layout")
        # self.window.bind("<Return>", self.finalize_current_border)

        # self.current_object = None  # Initially no object selected
        self.current_border = None  # Initially no border object being created
        self.current_road = None
        self.current_prohibited = None
        self.current_entrance = None
        self.start_x = None
        self.start_y = None
        self.is_starting = False 
        self.objects = []  # List to store all park objects
        # Create menu frame
        self.menu_frame = tk.Frame(self.window, width=100, height=500, bg="lightgray")
        self.menu_frame.pack(side="left")

        #TODO Remove the bloat
        # Load button icons
        self.road_icon = self.create_image("icons\\road.png")
        self.border_icon = self.create_image("icons\\border.png")
        self.entrance_icon = self.create_image("icons\\entrance.png")
        self.prohibited_icon = self.create_image("icons\\prohibited.png")
        self.selector_icon = self.create_image("icons\\selector.png")

        self.canvas = tk.Canvas(self.window, width=500, height=500)
        self.canvas.bind("<Button-1>", self.handle_click_on_canvas)
        self.canvas.pack()

        # Create buttons (with icons)

        self.current_object = None
        self.selector_button = tk.Button(self.menu_frame, text="Selector Tool", image=self.selector_icon, compound=tk.LEFT, command=lambda: self.set_object("selector"), bg="lightgray")
        self.selector_button.pack(pady=10)
        self.road_button = tk.Button(self.menu_frame, text="Road", image=self.road_icon, compound=tk.LEFT, command=lambda: self.set_object("road"), bg="lightgray")
        self.road_button.pack(pady=10)
        self.border_button = tk.Button(self.menu_frame, text="Border", image=self.border_icon, compound=tk.LEFT, command=lambda: self.set_object("border"), bg="lightgray")
        self.border_button.pack(pady=10)
        self.entrance_button = tk.Button(self.menu_frame, text="Entrance", image=self.entrance_icon, compound=tk.LEFT, command=lambda: self.set_object("entrance"), bg="lightgray")
        self.entrance_button.pack(pady=10)
        self.prohibited_button = tk.Button(self.menu_frame, text="Prohibited", image=self.prohibited_icon, compound=tk.LEFT, command=lambda: self.set_object("prohibited"), bg="lightgray")
        self.prohibited_button.pack(pady=10)
        # Create buttons with proper event binding
        # self.road_button.bind("<Button-1>", self.set_object("road"))
        # self.border_button.bind("<Button-1>", self.set_object("border"))
        # self.entrance_button.bind("<Button-1>", self.set_object("entrance"))
        # self.prohibited_button.bind("<Button-1>", self.set_object("prohibited"))
        # self.selector_button.bind("<Button-1>", self.set_object("selector"))

        # Canvas and other initialization   
        # self.objects = []
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

        # Update current_object based on the clicked button text
        #TODO Debloat the IFs, maybe make self.current_object self.current_object_name, make current_object hold the actual object
        if self.current_object == "road":
            self.objects.append(self.current_road)
        elif self.current_object == "border":
            self.objects.append(self.current_border)
        elif self.current_object == "entrance":
            self.objects.append(self.current_entrance)
        elif self.current_object == "prohibited":
            self.objects.append(self.current_prohibited)
        
        if text == "road":
            self.current_object = "road"
        elif text == "border":
            self.current_object = "border"
            self.current_border = Border(self.canvas)
        elif text == "entrance":
            self.current_object = "entrance"
        elif text == "prohibited":
            self.current_object = "prohibited"
            self.current_prohibited = ProhibitedZone(self.canvas)
        elif text == "selector":
            self.current_object = "selector"
            self.selector = Selector()
        else:
            # Handle unexpected button text (optional)
            print(f"Unknown object type: {text}")
        print(self.current_object)

    def handle_click_on_canvas(self, event):
        if self.current_object == "road":
            if self.is_starting is False:
                self.start_x = event.x
                self.start_y = event.y
                self.is_starting = True
                #self, canvas, start_x, start_y, end_x, end_y, width=5, color="#000000"
            else:
                self.is_starting = False
                self.current_road = Road(self.canvas, self.start_x, self.start_y, event.x, event.y)  
        elif self.current_object == "border":  
            x = event.x
            y = event.y
            print('test')
            if self.current_border:  # Check if a current border exists
                self.current_border.add_point(x, y)  # Add point to the current border
            else:
                self.current_border = Border(self.canvas)  # Create a new border on first click
                self.current_border.add_point(x, y)
                self.objects.append(self.current_border)
        elif self.current_object == "entrance":
            if self.current_border:
                x = event.x
                y = event.y
                self.current_entrance = Entrance(self.canvas, self.current_border, x, y)  # Create entrance
            else:
                print("Please select a border to create an entrance")
        elif self.current_object == "prohibited":
            x = event.x
            y = event.y
            print('test')
            if self.current_prohibited:  # Check if a current border exists
                self.current_prohibited.add_point(x, y)  # Add point to the current border
            else:
                self.current_prohibited = ProhibitedZone(self.canvas)  # Create a new border on first click
                self.current_prohibited.add_point(x, y)
                self.objects.append(self.current_prohibited)
        elif self.current_object == "selector":
            print(self.objects)
            for object in self.objects:
                print(object.id)
                self.canvas.tag_bind(object.id, '<Button-1>', self.selector.print_object(object))
            
    # def finalize_current_border(self, event):
    # # Check if there's a current border
    #     if self.current_border:
    #         self.current_border.finalize()
    #         self.current_border = None  # Clear current border object     
    #         print('final')   

    def run(self):
        self.window.mainloop()

# Create and run the ParkLayout object
park_layout = ParkLayout()
park_layout.run()

#TODO Selector Tool
#TODO Preview before placing