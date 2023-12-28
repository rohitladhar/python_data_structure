class Node:
    def __init__(self,value):
        self.data = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0 

    def __len__(self):
        return self.n

    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n+1

    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.n = self.n + 1
            return
        
        curr = self.head
        while curr.next !=None:
            curr = curr.next
        curr.next = new_node
        self.n = self.n + 1

    def printing(self):
        new_node = Node(5)
        self.head = new_node
        return self.head.next

    def insert_after(self,after,value):
        new_node = Node(value)
        curr = self.head
        while curr != None:
            if curr.data == after:
                break
            curr = curr.next
        if curr != None:
            new_node.next = curr.next
            curr.next = new_node 
            self.n = self.n + 1
        else:
            print("Item not Found")
            return 

    def clear(self):
        self.head = None
        self.n = 0
        print

    def delete_head(self):
        if self.head != None:   
            self.head = self.head.next
    
    def delete_tail(self):
        curr = self.head
        num = 0
        if curr == None:
            print("Linked List is empty")
            return
        if curr.next == None:
            self.delete_head()
        while curr.next.next != None:
            curr = curr.next
        curr.next = None
        self.n = self.n -1    

    def delete_value(self,value):
        curr = self.head
        if curr == None:
            print("Linked List is empty")
            return
        if curr.data == value:
            self.delete_head()
            return
       
        while curr.next != None:
            if curr.next.data == value:
                break
            curr = curr.next
        if curr.next == None:
            print("Item not found")
        else:
            curr.next = curr.next.next

    def search(self,value):
        curr = self.head
        num = 0
        if curr == None:
            print("Empty Linked List")
            return
        while curr != None:
            if curr.data == value:
                print("Number index "+ str(num))
                return
            num = num + 1
            curr = curr.next
        print("Number is not found")
        return

    def search_index(self,index):
        curr = self.head
        pos = 0
        if curr == None:
            print("Linked List Empty")
            return
        while curr != None:
            if pos==index:
                print("value "+str(curr.data))
                return
            curr = curr.next
            pos = pos + 1
        return 


L = LinkedList()
L.append(1)
# L.append(2)
# L.append(3)
# L.append(4)
# L.insert_head(5)

# L.insert_after(4,30)
# print(L.__str__())
# L.delete_value(1)
# L.delete_tail()
# L.delete_head()
# L.search_index(10)
# L.search(4)
# print(L.__str__())
