mystring: str = input("Enter String: ")

new_string = mystring[len(mystring)-1:] + mystring[1:len(mystring)-1] + mystring[0:1]

print(new_string)