num = int(input("Enter number: "))

if(num > 1):
    for i in range(2,num):
        if(num%i == 0):
            print("This is not a prime number")
            print(i,"is divided by",num,",quotient is",num/i)
            break
    else:
        print("This is a prime number")
else:
    print(num,"is not a prime number")

