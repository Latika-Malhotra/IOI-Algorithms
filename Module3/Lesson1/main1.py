class fruit:
    def __init__(self,color, season, name):
        self.color= color
        self.season = season
        self.name = name
    def display(self):
        print(f"{self.name} is of color {self.color} and you can eat it in season  {self.season}")

mangoObject= fruit("yellow","summer","mango")
mangoObject.display()