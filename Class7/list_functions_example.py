fruit_list = ["Apple","Mango","banana","mango","papaya","orange"]

fruit_list.insert(1,"kiwi")
print(fruit_list)

fruit_list.append("guava")
print(fruit_list)

fruit_list.extend(["grapes" , "peach"])
print(fruit_list)

ind = fruit_list.index("mango")
print(ind)

fruit_list.remove("Mango")
print(fruit_list)

last_element = fruit_list.pop()
print("last element of the list is: {}".format(last_element))
print(fruit_list)


fruit_list.reverse()
print(fruit_list)

fruit_list_copy = fruit_list.copy()
print(fruit_list_copy)





