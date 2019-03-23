para  = input("Enter string: ")

mystring = ""

for c in para:
    if c in mystring:
        print("Current value is {}".format(mystring))
        print("Repeated {}".format(c))
    else:
        mystring = mystring + c