list1 = [1,2,3]
list2 = ['a','b','c']
mergedList = []
index = 0
while len(mergedList) != len(list1)+len(list2):
    mergedList.append([list1[index]])
    mergedList.append([list2[index]])
    index = index+1
print mergedList
