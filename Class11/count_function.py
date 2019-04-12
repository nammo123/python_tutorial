count = 0

def fun1():
    global count
    count = count + 1
    print("fun1 called")

def fun2():
    global count
    count = count + 1
    print("fun2 called")

def fun3():
    global count
    count = count + 1
    print("fun3 called")


fun1()
fun2()
fun3()
fun1()
fun1()
fun3()
fun3()
fun2()







