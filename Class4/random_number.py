import random

random_num = random.randint(1,5)

# print(num)

num = input("Enter any number between 1 to 5: ")

if (int(num)==random_num):
    print("you guessed correctly you won")
    print("random_num = {}".format(random_num))
else:
    print("sorry!")
    print("random_num = {}".format(random_num))
