para = input("Enter string: ")
mychar = inut("enter a char: ")
count = 0

for c in para:
    if c == mychar:
        print(count)
        break
count = count + 1

for i in range(0,len(para)):
    if para[i] == mychar
        print(i)
        break

#find last occurance

for i in range(len(para), len(para)-1, -1)
    print(i)

index = -1
for i in range(0,len(para)):
    if(para[i] == mychar):
        index = i
if(index == -1):
    print("Sorry")
else:
    print("Last occurance at index {}".format(index))
    