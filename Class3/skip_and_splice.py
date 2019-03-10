#odd number print

mystring = "123456789"

odd_num_string = mystring[0:len(mystring)]
odd_num_string = mystring[0:9]

odd_num_string = mystring[0:9:1]   #skip 1 number
odd_num_string = mystring[0:9:2]   #skip 2 numbers


print(odd_num_string)

#even number print

mystring1 = "12345678910"

even_num_string = mystring1[1:len(mystring1):2]
print(even_num_string)

#print only 5

mystring3 = "123456789"

exact_num_string:str = mystring3[4]
print(exact_num_string)

