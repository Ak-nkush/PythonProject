# there is a difference between is a rel

class Mammal :
      def __init__(self,name,lifespan,habitat):
        #    constructor chaining
        self.name=name
        self.lifespan=lifespan
        self.habitat=habitat
        print("Mammal Object is created")

      def describe(self):
          print("Name:",self.name)
          print("Lifespan:",self.lifespan)
          print("Habitat:",self.habitat)

class Bat(Mammal) :
    def __init__(self,nm,lf,hb,diet):
        super().__init__(nm,lf,hb)
        self.diet = diet
        print("Bat object is created")

    # def describe(self):
    #     # super().describe()
    #     print("Diet of the bat is " , self.diet)


animal1 = Mammal("Bat",20,"j")
print(animal1.describe())
batObj = Bat("Bat",20,"j" , "insects")
print(batObj.describe())
