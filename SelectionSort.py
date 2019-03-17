#sample list
list1 = [34,67,12,89,45]

for i in range(len(list1)):
    
    min_index =i
    for j in range(i+1,len(list1)):
        if(list1[min_index] > list1[j]):
            min_index = j
    
    temp = list1[i]
    list1[i] = list1[min_index]
    list1[min_index] = temp

print(list1)    
