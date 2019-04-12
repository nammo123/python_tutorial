a = 10

def fun(x):
    global a
    print(a)
    a = 3
    res = 1

    for i in range(0,a):
        res = res * x
    return res

b = 5
res = fun(b)
print(res)
print(a)






