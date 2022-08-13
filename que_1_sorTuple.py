# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
tuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

# result = sorted(list,key= lambda x:x [-1])
Len = len(tuple)
for i in range(0,Len):
    for j in range(0,(Len -i - 1)):
        if(tuple[j][1] > tuple[j+1][1]):
            temp = tuple[j]
            tuple[j] = tuple[j+1]
            tuple[j+1] = temp


print(tuple)