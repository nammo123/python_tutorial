limit = int(input("Enter limit: "))
num = int(input("division number: "))
output_string = "Numbers divisible by {} between 0 to {} are: ".format(num,limit)


for i in range(0, limit+1):
    print(i)
    if i>=100:
        continue
    if(i%num == 0):
        output_string = output_string + str(i) + ","

print(output_string[:-1])