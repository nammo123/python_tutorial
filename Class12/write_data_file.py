with open("fruits.txt","w") as myfile:

    myfile.write("mango\n")
    myfile.write("apple\n")
    fruit_list = []

    while(True):
        fruits = input("Enter a fruit: (type 'exit' to end loop) ")
        if fruits == 'exit':
            break
        fruits = fruits + "\n"
        fruit_list.append(fruits)


    myfile.writelines(fruit_list)
