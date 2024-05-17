class PivotPoints():
    def __init__(self):
        self.points = []
    
    def __repr__(self):
        return self.points
    
    def append_points(self, object_points):
        for i in object_points:
            self.points.append(i)
        
    

    