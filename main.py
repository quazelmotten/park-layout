import tkinter as tk

class ParkGUI:
    def __init__(self):
        self.points = []
        self.entrances = []

        # Initialize the Tkinter window
        self.root = tk.Tk()
        self.root.title("Park Layout")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        # Bind mouse click event to handle placing points
        self.canvas.bind("<Button-1>", self.place_point)

        # Bind keyboard event to finish placing points and display the park
        self.root.bind("<Return>", self.finish_layout)

        # Display instructions
        self.canvas.create_text(250, 250, text="Click to place points", font=("Arial", 18), fill="black")

    def place_point(self, event):
        x = event.x
        y = event.y
        self.canvas.create_oval(x-2, y-2, x+2, y+2, fill="black")
        self.points.append((x, y))

    def finish_layout(self, event):
        self.canvas.delete("all")
        self.canvas.create_text(250, 250, text="Park Layout", font=("Arial", 18), fill="black")
        self.canvas.create_polygon(self.points, outline="green", fill="green", width=2)

        # Bind mouse click event for placing entrances
        self.canvas.bind("<Button-1>", self.place_entrance)
        self.root.bind("<Return>", self.display_entrances)

        # Display instructions
        self.canvas.create_text(250, 20, text="Click on the border to place entrances", font=("Arial", 12), fill="black")
        self.canvas.create_text(250, 40, text="Press Enter to finish", font=("Arial", 12), fill="black")

    def place_entrance(self, event):
        x = event.x
        y = event.y

        if self.is_on_border(x, y):
            self.canvas.create_oval(x-4, y-4, x+4, y+4, fill="blue")
            self.entrances.append((x, y))

    def is_on_border(self, x, y):
        for i in range(len(self.points)):
            x1, y1 = self.points[i]
            x2, y2 = self.points[(i + 50) % len(self.points)]

            if (x == x1 and y1 < y < y2) or (x == x2 and y2 < y < y1) or (y == y1 and x1 < x < x2) or (y == y2 and x2 < x < x1):
                return True

        return False

    def display_entrances(self, event):
        self.canvas.unbind("<Button-1>")
        self.root.unbind("<Return>")

# Create a park GUI object
park_gui = ParkGUI()

# Start the Tkinter event loop
park_gui.root.mainloop()