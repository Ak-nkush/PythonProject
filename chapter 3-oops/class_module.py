class City :
    # constructor is called once at the time of the object creation
    # self point to the current object
    # this is the parametrized constructor that takes parameter and assign the values to the object
    # init method act as a constructor
    def __init__(self, name,population):
        # self is the  generic name of the object
        self.name = name
        self.population = population

    #    method that is use to print details of the object
    def describeCity(self):
        print(f"The name of the city is {self.name}")
        print(f"The population is {self.population}")

# creating the another class in this file
class State :
    # building the constructor
    def __init__(self,name):
        self.name = name

#     describing the name of the state using a method
    def describeState(self):
        print(f"{self.name} is the state we are taking about")

# here we are giving the name to the object , the object we are creating in the class City
# mumbai = City("Mumbai","100000")
# mumbai.describeCity()

