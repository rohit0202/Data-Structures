list1 = [34,67,12,89,45]

y=0

for i in range(len(list1)):
    for j in range(0,len(list1)-1-i):
        if(list1[j] > list1[j+1]):
            temp = list1[j]
            list1[j] = list1[j+1]
            list1[j+1] = temp
        

print(list1)
