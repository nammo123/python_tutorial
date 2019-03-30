para = input("Enter comma seperated words: ")

word_list = para.split(",")


freq_dict = {}

for word in word_list:
    if word in freq_dict:
        val = freq_dict[word]
        val = val + 1
        freq_dict[word] = val
    else:
        freq_dict[word] = 1
print(freq_dict)

print(freq_dict["mango"])


max = -1
max_fruit = ""

for key in freq_dict:
    if freq_dict[key] > max:
        max = freq_dict[key]
        max_fruit = key

print(max_fruit)
print(max)
