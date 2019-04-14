def mainFunction():
    c = input("1. Login 2. Sign up")
    if c == '1':
        ph_no = input("Enter phpne number: ")
        pwd = input("Enter password: ")
        data = checkLogin(ph_no,pwd)

        if data == '-1':
            print("you are a first time user. please sign up.")
        elif data == '-2':
            print("wrong password")
        else:
            print("Login successfully")
            print(data)
    elif c == "2":
        user_data = []
        name = input("enter your name: ")
        address = input("Enter address: ")
        ph_no = input("Enter phone no: ")
        pwd = input("Enter password: ")
        data = input("Enter data: ")
        user_data.append(name)
        user_data.append(address)
        user_data.append(ph_no)
        user_data.append(data)

        res = createNewUser(user_data)

    else:
        print("wrong data")




