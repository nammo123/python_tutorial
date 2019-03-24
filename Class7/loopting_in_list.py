fruit_list = ["Apple","Mango","banana"]

fruit_list.append("Orange")
fruit_list.insert(2,"new fruit")

print(fruit_list)

#looping using for loop
result = "Fruits in my basket are: "

for fruit in fruit_list:
    #print(fruit)
    result = result + fruit + " "
print(result)

#looping using index

for i in range(0,len(fruit_list)):
    print(fruit_list[i])


