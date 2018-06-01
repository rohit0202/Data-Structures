class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    

class Linked_list_intersection:
    
    def __init__(self):
        self.head = None
        
    
    def add(self,item):
        
        temp = Node(item)
        temp.next = self.head
        self.head = temp
    
    def length(self):
        counter =0
        current = self.head
        
        while(current != None):
            current = current.next
            counter = counter +1
        
        #print(counter)
        return counter
    
    @staticmethod
    def merge_point(linked_list1,linked_list2):
        
        merge_point= None
        
        length_ll1 =linked_list1.length() 
        length_ll2 = linked_list2.length()
        
        if(length_ll1 == length_ll2):
            current1= linked_list1.head
            current2 = linked_list2.head
            
            while(current1.data != current2.data):
                current1 = current1.next
                current2 = current2.next
        
        elif(length_ll1 > length_ll2):
            
            counter = length_ll1 - length_ll2
            
            current1= linked_list1.head
            current2 = linked_list2.head
            
            while(counter !=0):
                current1 = current1.next
                counter = counter -1
            
            while(current1.data != current2.data):
                current1 = current1.next
                current2 = current2.next
                
                
        elif(length_ll2 > length_ll2):
            
            counter = length_ll2 - length_ll1
            
            current1 = linked_list1.head
            current2 = linked_list2.head
            
            while(counter != 0):
                current2 = current2.next
                counter = counter -1
                
            while(current1.data != current2.data):
                current1 = current1.next
                current2 = current2.next
        
             
        merge_point = current1

        return merge_point        


linked_list1= Linked_list_intersection()
#linked_list1.add(45)
linked_list1.add(99)
linked_list1.add(90)
linked_list1.add(78)
linked_list1.add(56)
linked_list1.add(45)
linked_list1.add(9)
linked_list1.add(4)
linked_list1.add(1)

#length_ll1= linked_list1.length()

linked_list2= Linked_list_intersection()
linked_list2.add(99)
linked_list2.add(90)
linked_list2.add(78)
linked_list2.add(11)
linked_list2.add(7)

#length_ll2 = linked_list2.length()

merge_point_object = Linked_list_intersection.merge_point(linked_list1, linked_list2)

print(merge_point_object.data)

