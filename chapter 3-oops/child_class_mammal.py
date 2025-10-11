from inheritance import Mammal
class Bat(Mammal) :
    def __init__(self,name,lifespan,habitat,diet):
        super().__init__(self,name,lifespan,habitat)
        self.diet = diet
        print("Bat object is created")

    def describe(self):
        print("Diet of the bat is " , self.diet)