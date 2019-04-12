#how much money a customer has spent

def moneySpentByCust(phone,customers):
    cust_data = customer[phone]
    shopping_dict = cust_data[3]
    sum = 0
    for key in shopping_dict:
        shopping_list = shoping_dict[key]
        for item in shopping_list:
            sum = sum + item[2] * item[3]
    return sum

#first purchase of data

def firstpurchase(phone,customers):
    first_item = ""
    if phone in customers:
        cust = customers[phone]
        shopping_dict = cust[3]
        if shopping_dict:
            first_shopping_cart = shopping_dict[1]
            if first_shopping_cart:
                first_item_data = first_shopping_cart[0]
                first_item = first_item_data[1]
                return first_item
        return first_item

#create data

def createData():
    customers = {}
    cust1 = ["mukund", 20,"HSR", {
    1: [[444,"moto e4", 10000,1],[555,"black shirt",1000,4],[666,"TV",20000,1]],
    2: [[222,"cricket bat",400,3],[777,"tennis ball",100,10]]}, "prime"]
    cust2 = ["john", 50,"Koramangala", {
    1: [[22,"washing machine", 20000,2],[33,"shoes",900,5],[44,"Vegatables",20,10]],
    2: [[567,"bed",14000,2],[788,"car wash",800,1]],
    3: [[890,"sofa set",50000,1]]},"not prime"]
    customers[9611218765]= cust1
    customers[9611213490]= cust2
    return customers

#main prog

def mainProgram():
    cust_dict = createData()
    user_phone_number = int(input("What's your phone no :"))
    total_money_spent = moneySpentByCust(user_phone_number,cust_dict)
    first_purchase_item = firstpurchase(user_phone_number,cust_dict)

    name = cust_dict[user_phone_number][0]


#calling main program first

if __name__ =='__main__':
    mainProgram()




#phone = int(input("What's your phone no :"))

#shopping_list_key_1 = 1
#if phone in customers:
#    shopping_dict = customers[phone][3]
#    if shopping_list_key_1 in shopping_dict:
#        item1 = shopping_dict[shopping_list_key_1]
#       print(item1[0][1])
#    else:
#        print("You have never shopped with us. Her are some exciting dicounts for you.")
#else:
#    print("Sorry could not find your details. Please create an account with us")





