import tkinter as tk
from ParkObject import ParkObject  # Import ParkObject from the objects folder
from objects.Road import Road  # Import Road from the objects folder
from objects.Border import Border
from objects.Entrance import Entrance
from objects.Prohibited import ProhibitedZone
from objects.Selector import Selector
from objects.PivotPoints import PivotPoints

#TODO Entrances follow the border angle
#TODO Preview before placing
#TODO Simple simulation
#TODO Small color change for borders and objects so that you could differentiate them
#TODO Highlight the selected object (for example, the red outline)
#TODO Pivot point highlight 
#TODO Sink active buttons
#TODO Top Menu
#TODO Alt-Mode that adds the object information on top of the object (like Current Border 0x01203BVB above the border)
#TODO Add Warning windows for no object selected, no border selected, etc
#TODO Fix Delete button

class ParkLayout:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Park Layout")
        self.window.geometry("1920x1080")
        self.window.state('zoomed')
        # self.window.bind("<Return>", self.finalize_current_border)

        # self.current_object = None  # Initially no object selected
        self.current_border = None  # Initially no border object being created
        self.current_road = None
        self.current_prohibited = None
        self.current_entrance = None
        self.selected_object = None
        self.start_x = None
        self.start_y = None
        self.is_starting = False 
        self.is_road_finalized = False
        self.selector = Selector()
        self.objects = []
        self.pivot_points = PivotPoints()  # List to store all park objects
        # Create menu frame
        # self.menu = tk.Menu(self)
        # self.file_menu = tk.Menu(self.menu, tearoff=0)
        # self.file_menu.add_command(label="Новый файл")

        top_left_square_size = 110
        self.window.grid_rowconfigure(1, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        self.top_left_square = tk.Frame(self.window, width=top_left_square_size, height=25, bg="grey")
        self.top_left_square.grid(row=0, column=0)
        self.ui_label = tk.Label(self.top_left_square, text="Park Layout")
        self.ui_label.pack()

        # Create top menu frame
        self.top_menu_frame = tk.Frame(self.window, height=top_left_square_size, highlightbackground="black", highlightthickness=1, bg="lightblue")
        self.top_menu_frame.grid(row=0, column=1, sticky="ew")

        # Create left menu frame
        self.left_menu_frame = tk.Frame(self.window, width=top_left_square_size, highlightbackground="black", highlightthickness=1, bg="lightgray")
        self.left_menu_frame.grid(row=1, column=0, sticky="ns")

        # Create bottom text frame

        # Create center canvas frame
        self.center_frame = tk.Frame(self.window)
        self.center_frame.grid(row=1, column=1, sticky="nsew")

        # Create the canvas
        self.canvas = tk.Canvas(self.center_frame, bg="white")
        self.canvas.bind("<Button-1>", lambda e: self.handle_click_on_canvas(e))
        self.canvas.bind("<Motion>", lambda e: self.handle_motion_on_canvas(e))
        self.canvas.pack(expand=True, fill="both")
        
        self.bottom_text_frame = tk.Frame(self.window, height=25, bg="lightgreen")
        self.bottom_text_frame.grid(row=2, column=0, columnspan=2, sticky="ew")
        self.status_text = tk.Text(self.bottom_text_frame, height=1, state='disabled', bg='lightgreen')
        self.status_text.pack(fill="both",expand=True)

        # self.text_field = tk.Text(height='25',state='disabled')
        # self.text_field.pack(side='bottom',anchor='sw')
        # self.config(menu=self.menu)
        

        #TODO Remove the bloat
        # Load button icons
        self.road_icon = self.create_image("icons\\road.png")
        self.border_icon = self.create_image("icons\\border.png")
        self.entrance_icon = self.create_image("icons\\entrance.png")
        self.prohibited_icon = self.create_image("icons\\prohibited.png")
        self.selector_icon = self.create_image("icons\\selector.png")
        self.pivot_icon = self.create_image("icons\\pivot.png")
        self.delete_icon = self.create_image("icons\\delete.png")

        button_width = 100

        # Create buttons (with icons)
        self.current_object = None
        self.selector_button = tk.Button(self.top_menu_frame, text="Selector Tool", image=self.selector_icon, compound=tk.LEFT, command=lambda: self.set_object("selector"), bg="lightgray", width=button_width)
        self.selector_button.pack(side=tk.LEFT)
        self.road_button = tk.Button(self.left_menu_frame, text="Road", image=self.road_icon, compound=tk.LEFT, command=lambda: self.set_object("road"), bg="lightgray", width=button_width)
        self.road_button.pack()
        self.border_button = tk.Button(self.left_menu_frame, text="Border", image=self.border_icon, compound=tk.LEFT, command=lambda: self.set_object("border"), bg="lightgray", width=button_width)
        self.border_button.pack()
        self.entrance_button = tk.Button(self.left_menu_frame, text="Entrance", image=self.entrance_icon, compound=tk.LEFT, command=lambda: self.set_object("entrance"), bg="lightgray", width=button_width)
        self.entrance_button.pack()
        self.prohibited_button = tk.Button(self.left_menu_frame, text="Prohibited", image=self.prohibited_icon, compound=tk.LEFT, command=lambda: self.set_object("prohibited"), bg="lightgray", width=button_width)
        self.prohibited_button.pack()
        self.pivot_button = tk.Button(self.top_menu_frame, text="Pivot", image=self.pivot_icon, compound=tk.LEFT, command=self.pivot_button_press, bg="lightgray", width=button_width)
        self.pivot_button.pack(side=tk.LEFT)
        self.delete_button = tk.Button(self.top_menu_frame, text="Delete", image=self.delete_icon, compound=tk.LEFT, command=self.delete_button_press, bg="lightgray", width=button_width)
        self.delete_button.pack(side=tk.LEFT)
    
    def update_bottom_text(self):
        self.status_text.config(state="normal")
        self.status_text.delete(1.0, tk.END)
        self.status_text.insert(tk.END, f'Selected object:{self.selector.selected_object}; Current object:{self.current_object}, Pivot{' enabled' if self.pivot_points.is_sunken else ' disabled'}')
        self.status_text.config(state='disabled')

    def create_image(self, filename):
    # Implement logic to create a square image from a file (considering size)
    # You can use libraries like PIL (Pillow) for image manipulation
    # This function should return a PhotoImage object suitable for the button
        from PIL import Image, ImageTk  # Assuming you have PIL installed
        image = Image.open(filename).resize((20, 20))  # Resize image to 20x20 pixels
        return ImageTk.PhotoImage(image)

    def pivot_button_press(self):
        if self.pivot_points.is_sunken:
            self.pivot_button.config(relief='raised')
        else:
            self.pivot_button.config(relief='sunken')
        self.pivot_points.set_sunken()
        self.update_bottom_text()
    
    def delete_button_press(self):
        if isinstance(self.selector.selected_object, Border):
            self.canvas.delete(self.selector.selected_object.id)
            self.objects.remove(self.selector.selected_object)
            for point in self.selector.selected_object.points:
                self.pivot_points.points.remove(point)
            for entrance in self.selector.selected_object.entrances:
                self.canvas.delete(entrance.id)
                self.objects.remove(entrance)
            self.selector.selected_object = None
            print(self.selector.selected_object)
        elif self.selector.selected_object:
            self.canvas.delete(self.selector.selected_object.id)
            self.objects.remove(self.selector.selected_object)
            for point in self.selector.selected_object.points:
                self.pivot_points.points.remove(point)
            self.selector.selected_object = None
            print(self.selector.selected_object)
        else:
            print('There\'s no object selected')
        self.update_bottom_text()

    def set_object(self, text):
        #TODO Debloat the IFs, maybe make self.current_object self.current_object_name, make current_object hold the actual object
        if self.current_object == "road":
            self.is_starting = False
        if self.current_object == "border":
            self.objects.append(self.current_border)
            self.pivot_points.append_points(self.current_border.points)
        elif self.current_object == "prohibited":
            self.objects.append(self.current_prohibited)
            self.pivot_points.append_points(self.current_prohibited.points)
        elif self.current_object == "selector":
            self.canvas.unbind_all("<Button-1>")
            self.canvas.bind("<Button-1>", lambda e: self.handle_click_on_canvas(e))
            
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
            print(self.objects)
            for object in self.objects:
                print(object.id)
                self.canvas.tag_bind(object.id, '<Button-1>', lambda e,o=object,c=self.canvas: self.selector.print_object(e,o,canvas=c))
        else:
            # Handle unexpected button text
            print(f"Unknown object type: {text}")
        print(self.current_object)
        self.update_bottom_text()

    def handle_motion_on_canvas(self, event):
        # print(f'Motion on {event.x,event.y}')
        return

    def handle_click_on_canvas(self, event):
        if self.current_object == "road":
            if self.is_starting is False:
                start_points = self.pivot_points.find_closest_pivot_point(self.pivot_points.points,event.x,event.y)
                self.start_x, self.start_y = start_points
                self.is_starting = True
            else:
                end_points = self.pivot_points.find_closest_pivot_point(self.pivot_points.points,event.x,event.y)
                end_x, end_y = end_points
                self.current_road = Road(self.canvas, self.start_x, self.start_y, end_x, end_y)  
                self.start_x, self.start_y = end_points
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
            print(self.selector.selected_object)
            # if "Border" in str(self.selector.selected_object): #isinstance
            self.current_border = self.selector.selected_object
            if self.current_border:
                start_points = self.pivot_points.find_closest_pivot_point(self.pivot_points.points,event.x,event.y)
                x, y = start_points
                self.current_entrance = Entrance(self.canvas, self.current_border, x, y)
                self.objects.append(self.current_entrance) 
                self.current_border.entrances.append(self.current_entrance)
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
        
                # self.canvas.tag_bind(object.id, '<Button-1>', lambda x: self.delete_object(object))
        elif self.current_object == 'pivot':
            print(f'Pivot Points:{self.pivot_points.points}')
        self.update_bottom_text()

    def delete_object(self, object):
        self.canvas.delete(object.id)
        self.objects.remove(object)
        for point in object.points:
            self.pivot_points.remove(point)

    def run(self):
        self.window.mainloop()

# Create and run the ParkLayout object
park_layout = ParkLayout()
park_layout.run()