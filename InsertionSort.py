list1 = [67,34,12,89,45]


for i in range(1,len(list1)):
    
    key = list1[i]
    
    j=i-1
    while(j >=0 and key < list1[j]):
        list1[j+1] = list1[j]

        list1[j] = key 
        j = j-1
    
print(list1)
