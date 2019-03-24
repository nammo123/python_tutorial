from typing import List, Union

dish1 = [1,"Chinees noodles", ["noodles","chilli","salt","soya souce","egg"], 250.50, "s", 'Veg']

dish2 = [2,"Fried rice", ["rice","salt","egg"],300.45,"m","veg"]

dish3 = [3,"ice cream",["milk","sugar","flavors"],100.5,"d","veg"]

dish4 = [4,"fried babycorn",["corn","tomato"],220.4,"s", "veg"]

menu = [dish1, dish2, dish3, dish4]

print("all dishes with egg")
count = 0
for dish in menu:
    ingredients_result = dish[2]
    if "egg" in ingredients_result:
        count = count + 1
        print("option {} : dish name is {} , price is {}".format(count,dish[1],dish[3]))

print("all starters")

for dish in menu:
    ingredients_result1 = dish[4]
    if "s" in ingredients_result1:
        print("starter name is {}, price is {}".format(dish[1],dish[3]))

print("Calculate bill function")

purchased_bill = []
while(true):
    id = int(input("enter id of the dish (enter 0 for exit): "))
    if id == 0:
        print






