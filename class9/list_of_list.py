fruit_list = [["mango","king of fruit"],["kiwi","costly fruit"], ["orange","vitamin c"]]


fruit_name = input("Enter fruit name: ")

for fruit in fruit_list:
    if fruit_name in fruit:  #if fruit_name == fruit[0]
        print("{} is {}". format(fruit_name,fruit[1]))
        break 
