fruit_dictionary = {"mango": "king of fruits", "kiwi": "costly fruit"}

fruit_dictionary["orange"] = "vitamin c"

fruit_dictionary["apple"] = "an apple a day , keeps a doctor away"

for key in fruit_dictionary.keys():
    print("key : {} , value : {} ".format(key,fruit_dictionary[key]))

for val in fruit_dictionary.values():
    print(val)


for key,val in fruit_dictionary.items():
    print(key)
    print(val)