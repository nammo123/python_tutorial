name = input("Enter name: ")
address = input("Enter address: ")
salary = input("Monthly salary: ")
spent = input("how much you spent this month: ")

balance = float(salary)-float(spent)

message1 = "Hi, {0}, you are living in {1}. You have spent {2} rupees this month. Your remaining balance is {3} rupees.".format(name,address,spent,balance)
message2 = "Note that your monthly salary is {0}".format(salary)

print(message1+message2)



