import math
# encapsulation = getter and setter , creating a security layer
class Circle :
    def __init__(self, rad):
        # constructor is not responsible for creating the limitation on the user input
        # for that we are using setter
        self.set_radius(rad)

    def set_radius(self,rd):
        self._radius = rd
        print("Radius is set")

    def get_radius(self):
            return self._radius

    def computeArea(self):
        rdtmp = self.get_radius()
        area = math.pi * (rdtmp ** 2)
        return area


mycir = Circle(2)
print(mycir.computeArea() , f"is the area of the circle having radius {mycir.get_radius()}")