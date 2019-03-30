
fruit_dictionary = {"mango": "king of fruits", "kiwi": "costly fruit"}

fruit_dictionary["orange"] = "vitamin c"

fruit_dictionary["apple"] = "an apple a day , keeps a doctor away"

print(fruit_dictionary)

fruit_name = input("fruit name: ")

#if fruit_name in fruit_dictionary:
#    fruit_desc = fruit_dictionary[fruit_name]
#    print("{} is {}".format(fruit_name,fruit_desc))
#else:
#    print("sorry")

fruit_desc = fruit_dictionary.get(fruit_name)

if fruit_desc != None:
    print("{} is {}".format(fruit_name, fruit_desc))
else:
    print("sorry")
