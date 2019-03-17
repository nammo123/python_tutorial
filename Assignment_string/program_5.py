word1 = input("Enter word1: ")
word2 = input("enter word2: ")


new_word1 = word1[0:2] + word2[2:]
new_word2 = word2[0:2] + word1[2:]

first_word = new_word1.split(" ")
sec_word = new_word2.split(" ")
new_word = first_word + sec_word
print(new_word)




