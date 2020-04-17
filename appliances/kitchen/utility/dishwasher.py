from appliances.appliance import Appliance

class DishWasher(Appliance):

    def __init__(self, color):
        super().__init__(color)
        self.clean = True
        self.dishes = []

    def wash_dishes(self):
        print("grind, grind, clunk. Time to call the repair person")
