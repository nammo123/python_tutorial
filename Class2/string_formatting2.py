name = input("Enter your name : ")
address = input("Enter your address: ")

message = "Hello {} , Welcome to {}.".format(name,address)  # directly assign stering formatting 
print(message)

message_after_replacement = message.format(name,address)  #store format value to new string
print(message_after_replacement)

message = "Hello {0} , Welcome to {1}. I am glad that {0} is in {1}".format(name,address)  #giving indexing
print(message)
