mystring = input("Enter String: ")

# print first two and last two character

word1 = mystring[0:2]
word2 = mystring[len(mystring) - 2:len(mystring)]
ans = word1 + word2

#word3 = mystring[0]


if len(mystring) >= 2:
    print(ans)
else:
    print("empty string!!")

