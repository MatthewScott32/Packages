from appliances.kitchen import DishWasher
from appliances.laundry import Dryer
from appliances.laundry import Washer
from appliances.kitchen import Refrigerator
from appliances import Appliance
from appliances.kitchen import CoffeeMaker
from appliances.kitchen import CanOpener

whirlpool_dishwasher = DishWasher("black")
print(f'{whirlpool_dishwasher.color}')
whirlpool_dishwasher.wash_dishes()

lg_fridge = Refrigerator("stainless")
print(f'{lg_fridge.color}')
lg_fridge.make_ice()

can_opener = CanOpener("silver")
print(f'{can_opener.color}')
can_opener.open_can()

mr_coffee = CoffeeMaker("white")
print(f'{mr_coffee.color}')
mr_coffee.make_coffee()

dryer = Dryer("yellow", "taco")
print(f'{dryer.color}')
dryer.dry_clothes("low")
dryer.dry_clothes("high")

samsung_washer = Washer("red")
print(f'{samsung_washer.color}')
samsung_washer.wash_clothes("normal")
samsung_washer.wash_clothes("delicates")
samsung_washer.wash_clothes("super_scrub")
