def common_data(list1,list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result

print(common_data([1,2,3,4], [2,4,6,8]))
print(common_data([1,3,5,7],[2,4,6,8]))




