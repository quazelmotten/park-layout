from math import inf,dist

class PivotPoints():
    def __init__(self):
        self.points = []
        self.is_sunken = False
    
    def __repr__(self):
        return self.points
    
    def set_sunken(self):
        if self.is_sunken:
            self.is_sunken = False
        else:
            self.is_sunken = True
    
    def append_points(self, object_points):
        for i in object_points:
            self.points.append(i)

    def find_closest_pivot_point(self,points,x,y):
        if self.is_sunken:
            if points:
                min_dist = inf
                for i in points:
                    if dist(i,(x,y)) < min_dist:
                        min_point = i
                        min_dist = dist(i,(x,y))
                return min_point 
        return (x,y)





        
    

    