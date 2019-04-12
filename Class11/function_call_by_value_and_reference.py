def modifyInt(a):
    print(a)
    a = 10
    print(a)

def modifyFloat(b):
    b = 10.5

def modifyString(c):
    c = "modified"

def modifyList(l):
    l.clear()
    l.append("change")
    l.append("0000")
    l.append("1.333")

def modifyDict(d):
    d[3] = "pqr"
    

#call by value

num_int = 100
print("Before modification {}".format(num_int))
modifyInt(num_int)
print("After modification {}".format(num_int))


num_float = 100.5
print("Before modification {}".format(num_float))
modifyFloat(num_float)
print("After modification {}".format(num_float))

var_string = "original"
print("Before modification {}".format(var_string))
modifyString(var_string)
print("After modification {}".format(var_string))

var_list = [1,2,3,4,5]
print("Before modification {}".format(var_list))
modifyList(var_list)
print("After modification {}".format(var_list))

var_dict = {1:"abc", 2: "xyz"}
print("Before modification {}".format(var_dict))
modifyDict(var_dict)
print("After modification {}".format(var_dict))








