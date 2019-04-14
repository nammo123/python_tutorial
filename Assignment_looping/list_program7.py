a = [10,20,40,40,50,20,30,60,70,10]

#dup_items = set()
unique_items = []

for i in a:
    if i not in unique_items:
        unique_items.append(i)
       # dup_items.add(i)
print(unique_items)