number= int(input("Enter the range number: "))

first_value = 0
second_value = 1
count = 0

for count in range(0,number+1):   #while(count < number)
    if(count <= 1):
        temp = count
    else:
        temp = first_value + second_value
        first_value = second_value
        second_value = temp
    print (temp)
    count = count + 1
