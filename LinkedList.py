#Basic operations on a linked list in python
class Node2:
    def __init__(self,data):
        self.data = data;
        self.next = None;



class LinkedList007:
    def __init__(self):
        self.head = None;
        
    
    def add(self,item):
        #adding a node at the front of a linked list        
        temp = Node2(item)
        temp.next = self.head
        self.head = temp
        

    def display(self):
        #displays the content of a linked list
        current = self.head
        
        while(current.next != None):
            print(current.data)
            current = current.next
        print(current.data)    
        
    def size(self):
        #prints the size of a linked list
        counter =0
        current = self.head
        
        while(current != None):
            counter = counter +1
            current = current.next
        
        print("The size of the linked list is : " + str(counter))



    def search(self,item):
        #searches an element in a linked list        
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
        #removes an item form the linked list, provided repitition is not there.
        
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
        #inserts an item/node at a specified position in a linked list.
        
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
        #removes the last element from the linked list.
        
        previous = None
        current = self.head
        
        while(current.next != None):
            previous = current
            current = current.next
            
        previous.next = None
        
    
    def index(self,item):
        #prints the index/position of a node/item
        
        counter =0
        current = self.head
        
        while(current.data != item):
            counter = counter +1
            current = current.next
                
        print("Index of " +str(item) + " is " + str(counter))

    def append(self,item):
        #appends an item/node at the end of the linked list.        
        current = self.head
        
        while(current.next != None):
            current = current.next
        
        current.next = Node2(item)
        
    
    def cycle(self):
        #creates a cycle in the linked list
        
        #current = self.head
        
        self.head.next.next.next.next.next = self.head.next
        
        
        
    def detect_cycle(self):
        #detects if a cycle is present in the linked list
        
        fast = self.head
        slow = self.head
        
        while(fast != None and slow != None and fast.next !=None):
            slow = slow.next
            fast = fast.next.next
            
            if(slow == fast):
                return "Cycle found " 
        return "Cycle not found"
    
    
    
    def detect_and_remove(self):
        #detects and removes the loop in a linked list
        
        fast = self.head
        slow = self.head
        
        while(fast != None and slow != None and fast.next !=None):
            slow = slow.next
            fast = fast.next.next
            
            if(slow == fast):
                break
            
        
        pointer1 = self.head
        
        pointer2 = slow
        
        while(pointer1.next != pointer2.next):
            pointer1 = pointer1.next
            pointer2 = pointer2.next
            
        pointer2.next = None
    

obj1 = LinkedList007()


obj1.add(89)
obj1.add(12)
obj1.add(45)
obj1.add(34)
obj1.add(72)


obj1.display()
obj1.size()
obj1.search(34)

obj1.remove(45)
obj1.display()
print("------------------------")
print("After insertion")
obj1.insert(72,55)
obj1.display()
print("--------------------------")
print("After poping")
obj1.pop()
obj1.display()
print("-----------------------------")
obj1.index(72)
print("----------------")
print("After appending")
obj1.append(88)
obj1.display()


obj1.cycle()

print("-------------------------------")
print("After cycle")
print(obj1.head.data)
print(obj1.head.next.data)
print(obj1.head.next.next.data)
print(obj1.head.next.next.next.data)
print(obj1.head.next.next.next.next.data)
print(obj1.head.next.next.next.next.next.data)
print(obj1.head.next.next.next.next.next.next.data)
print(obj1.head.next.next.next.next.next.next.next.data)
print(obj1.head.next.next.next.next.next.next.next.next.data)
print(obj1.head.next.next.next.next.next.next.next.next.next.data)

print("----------------------------------")
print("Detecting cycle")
print(obj1.detect_cycle())

print("----------------------------------")
print("removing cycle")
obj1.detect_and_remove()
print(obj1.detect_cycle())

print(obj1.head.data)
print(obj1.head.next.data)
print(obj1.head.next.next.data)
print(obj1.head.next.next.next.data)
print(obj1.head.next.next.next.next.data)
