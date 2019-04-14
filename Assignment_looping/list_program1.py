#items = int(input("Enter values: "))

def sum_list(items):
    count = 0
    for i in items:
        count = count + i
    return count

print(sum_list([1,4,-6]))
