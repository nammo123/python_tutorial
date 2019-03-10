year = int(input("Enter Year: "))

if( ((year%4==0) and (year%100!=0)) or (year%400==0)):
    print("It's a leap year")
else:
    print("Its not a leap year")

