para = input("enter string: ")

count = 0

for c in para:
    print(c)
    if c =="a" or c =="e" or c =="i" or c =="o" or c =="u":
        count = count +1

print("numbers of vovels are {}".format(count))



