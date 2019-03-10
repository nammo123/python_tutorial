para = input("Enter a senetence: ")

words = para.split(" ")  #split sentence on based of common thing

print(words)


print("No of words are {}".format(len(words)))


#even number print


even_num_string = words[1:len(words):2]
print(even_num_string)
