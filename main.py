import tkinter as tk
from ParkObject import ParkObject  # Import ParkObject from the objects folder
from objects.Road import Road  # Import Road from the objects folder
from objects.Border import Border
from objects.Entrance import Entrance
from objects.Prohibited import ProhibitedZone
from objects.Selector import Selector
from objects.PivotPoints import PivotPoints

#TODO Pivot Points
#TODO Multiline roads
#TODO Entrances follow the border
#TODO Make the entrance be placeable on any border, not just the last one
#TODO Preview before placing
#TODO Simple simulation

class ParkLayout:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Park Layout")
        self.window.state('zoomed')
        # self.window.bind("<Return>", self.finalize_current_border)

        # self.current_object = None  # Initially no object selected
        self.current_border = None  # Initially no border object being created
        self.current_road = None
        self.current_prohibited = None
        self.current_entrance = None
        self.start_x = None
        self.start_y = None
        self.is_starting = False 
        self.objects = []
        self.pivot_points = PivotPoints()  # List to store all park objects
        # Create menu frame
        # self.menu = tk.Menu(self)
        # self.file_menu = tk.Menu(self.menu, tearoff=0)
        # self.file_menu.add_command(label="Новый файл")
        self.top_menu_frame = tk.Frame(self.window, width=1920, height=25, bg="lightgray")
        self.top_menu_frame.pack(side='top', anchor='nw')
        self.menu_frame = tk.Frame(self.window, width=100, height=1080, bg="lightgray")
        self.menu_frame.pack(side="top", anchor='nw')
        # self.config(menu=self.menu)
        

        #TODO Remove the bloat
        # Load button icons
        self.road_icon = self.create_image("icons\\road.png")
        self.border_icon = self.create_image("icons\\border.png")
        self.entrance_icon = self.create_image("icons\\entrance.png")
        self.prohibited_icon = self.create_image("icons\\prohibited.png")
        self.selector_icon = self.create_image("icons\\selector.png")
        self.pivot_icon = self.create_image("icons\\pivot.png")

        self.canvas = tk.Canvas(self.window, width=1920, height=1080)
        self.canvas.bind("<Button-1>", self.handle_click_on_canvas)
        self.canvas.pack()

        # Create buttons (with icons)
        self.current_object = None
        self.selector_button = tk.Button(self.menu_frame, text="Selector Tool", image=self.selector_icon, compound=tk.LEFT, command=lambda: self.set_object("selector"), bg="lightgray")
        self.selector_button.pack()
        self.road_button = tk.Button(self.menu_frame, text="Road", image=self.road_icon, compound=tk.LEFT, command=lambda: self.set_object("road"), bg="lightgray")
        self.road_button.pack()
        self.border_button = tk.Button(self.menu_frame, text="Border", image=self.border_icon, compound=tk.LEFT, command=lambda: self.set_object("border"), bg="lightgray")
        self.border_button.pack()
        self.entrance_button = tk.Button(self.menu_frame, text="Entrance", image=self.entrance_icon, compound=tk.LEFT, command=lambda: self.set_object("entrance"), bg="lightgray")
        self.entrance_button.pack()
        self.prohibited_button = tk.Button(self.menu_frame, text="Prohibited", image=self.prohibited_icon, compound=tk.LEFT, command=lambda: self.set_object("prohibited"), bg="lightgray")
        self.prohibited_button.pack()
        self.pivot_button = tk.Button(self.top_menu_frame, text="Pivot", image=self.pivot_icon, compound=tk.LEFT, command=self.pivot_button_press, bg="lightgray")
        self.pivot_button.pack()
    def create_image(self, filename):
    # Implement logic to create a square image from a file (considering size)
    # You can use libraries like PIL (Pillow) for image manipulation
    # This function should return a PhotoImage object suitable for the button
        from PIL import Image, ImageTk  # Assuming you have PIL installed
        image = Image.open(filename).resize((20, 20))  # Resize image to 20x20 pixels
        return ImageTk.PhotoImage(image)

    def pivot_button_press(self):
        if self.pivot_points.is_sunken:
            self.pivot_button.config(relief='sunken')
            self.pivot_points.is_sunken=False
        else:
            self.pivot_button.config(relief='raised')
            self.pivot_points.is_sunken=True

    def set_object(self, text):
        # Get the button that was clicked

        # Get the text of the clicked button (lowercase for consistency)

        # Update current_object based on the clicked button text
        #TODO Debloat the IFs, maybe make self.current_object self.current_object_name, make current_object hold the actual object
        # if self.current_object == "road":
        #     self.objects.append(self.current_road)
        if self.current_object == "border":
            self.objects.append(self.current_border)
            self.pivot_points.append_points(self.current_border.points)
        # elif self.current_object == "entrance":
        #     self.objects.append(self.current_entrance)
        elif self.current_object == "prohibited":
            self.objects.append(self.current_prohibited)
            self.pivot_points.append_points(self.current_prohibited.points)
        elif self.current_object == "selector":
            self.canvas.unbind_all("<Button-1>")
        
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
                start_points = self.pivot_points.find_closest_pivot_point(self.pivot_points.points,event.x,event.y)
                self.start_x, self.start_y = start_points
                self.is_starting = True
            else:
                self.is_starting = False
                self.current_road = Road(self.canvas, self.start_x, self.start_y, event.x, event.y)  
                self.objects.append(self.current_road)
                self.pivot_points.append_points(self.current_road.points)
        elif self.current_object == "border":  
            start_points = self.pivot_points.find_closest_pivot_point(self.pivot_points.points,event.x,event.y)
            x, y = start_points
            print('test')
            if self.current_border:  # Check if a current border exists
                self.current_border.add_point(x, y)  # Add point to the current border
            else:
                self.current_border = Border(self.canvas)  # Create a new border on first click
                self.current_border.add_point(x, y)
        elif self.current_object == "entrance":
            if self.current_border:
                start_points = self.pivot_points.find_closest_pivot_point(self.pivot_points.points,event.x,event.y)
                x, y = start_points
                self.current_entrance = Entrance(self.canvas, self.current_border, x, y)
                self.objects.append(self.current_entrance) 
                self.pivot_points.append_points(self.current_entrance.points) # Create entrance
            else:
                print("Please select a border to create an entrance")
        elif self.current_object == "prohibited":
            start_points = self.pivot_points.find_closest_pivot_point(self.pivot_points.points,event.x,event.y)
            x, y = start_points
            print('test')
            if self.current_prohibited:  # Check if a current border exists
                self.current_prohibited.add_point(x, y)  # Add point to the current border
            else:
                self.current_prohibited = ProhibitedZone(self.canvas)  # Create a new border on first click
                self.current_prohibited.add_point(x, y)
        elif self.current_object == "selector":
            print(self.objects)
            for object in self.objects:
                print(object.id)
                # self.canvas.tag_bind(object.id, '<Button-1>', self.selector.print_object(object))
                self.canvas.tag_bind(object.id, '<Button-1>', lambda x: self.delete_object(object))
        elif self.current_object == 'pivot':
            print(f'Pivot Points:{self.pivot_points.points}')
    def delete_object(self, object):
        self.canvas.delete(object.id)
        self.objects.remove(object)

    def run(self):
        self.window.mainloop()

# Create and run the ParkLayout object
park_layout = ParkLayout()
park_layout.run()