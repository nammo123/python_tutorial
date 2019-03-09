mystring = input("please enter string")

trimmed_string = mystring.strip()

reverse = trimmed_string[len(trimmed_string)-1::-1]

print("original string is {}, and reverse string is {}".format(trimmed_string,reverse))



if trimmed_string ==reverse:
    print("It's a palindrome")
else:
    print("It's not a palindrome")