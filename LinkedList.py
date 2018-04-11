class Node:
    def __init__(self,data):
        self.data = data;
        self.next = None;



class LinkedList:
    def __init__(self):
        self.head = None;
        
    
    def add(self,item):
        #adds a node in the begining of the linked list        
        temp = Node(item)
        temp.next = self.head
        self.head = temp
        

    def display(self):
        #displays the contents of the linked list
        current = self.head
        
        while(current.next != None):
            print(current.data)
            current = current.next
        print(current.data)    
        
    def size(self):
        #displays the size of the linked list
        counter =0
        current = self.head
        
        while(current != None):
            counter = counter +1
            current = current.next
        
        print("The size of the linked list is : " + str(counter))



    def search(self,item):
        #searches for an item in the linked list
        
        current = self.head
        status ="Not Found"
        
        while(current != None):
            if(current.data == item):
                status = "Found"
                break
            else:
                current = current.next
        
        print(status)


    def remove(self,item):
        #removes a particular node from the linked list
        
        current = self.head
        previous = None
        
        while(current != None):
            if(current.data == item):
                break
            else:
                previous = current
                current = current.next
        
        if(previous == None):
            self.head = current.next
        else:
            previous.next = current.next
            
            
    def insert(self,after_item,item):
        #inserts a node anywhere in the linked list
        
        current = self.head
                
        while(current.data != after_item):
            current = current.next
            
        if(current.next != None):
            temp = current.next
            new_node = Node2(item)
            
            current.next = new_node
            new_node.next = temp
             
        else:
            new_node = Node2(item)
            current.next = new_node
            
             
    def pop(self):
        #deletes the last node of the linked list
        
        previous = None
        current = self.head
        
        while(current.next != None):
            previous = current
            current = current.next
            
        previous.next = None
        
    
    def index(self,item):
        #displays the index of a node in linked list
        
        counter =0
        current = self.head
        
        while(current.data != item):
            counter = counter +1
            current = current.next
                
        print("Index of " +str(item) + " is " + str(counter))

    def append(self,item):
        #inserts a node at the end of the linked list
        
        current = self.head
        
        while(current.next != None):
            current = current.next
        
        current.next = Node2(item)
         
 

obj1 = LinkedList()


obj1.add(89)
obj1.add(12)
obj1.add(45)
obj1.add(34)
obj1.add(72)
print("------------------------")

obj1.display()
obj1.size()
obj1.search(34)

obj1.remove(45)
obj1.display()
print("------------------------")
obj1.insert(72,55)
obj1.display()
print("--------------------------")
obj1.pop()
obj1.display()
print("-----------------------------")
obj1.index(72)
print("----------------")
obj1.append(88)
obj1.display()
