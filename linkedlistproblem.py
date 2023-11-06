# Maximum value replace with given value
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None 
        self.n = 0

    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            new_node.next = self.head
            self.head = new_node
            self.n = self.n + 1
        else:
            curr = self.head
            while curr.next !=None:
                curr = curr.next

            curr.next = new_node
            self.n = self.n + 1

    def transverse(self):
        curr = self.head
        result = ''
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    def replace_value(self,item):
        temp = self.head
        max = temp
        while temp != None:
            if max.data<temp.data:
                max = temp
            temp = temp.next

        max.data = item
        
        
       

L = Linkedlist()
L.append(1)
L.append(2)
L.append(3)
print(L.transverse())
L.replace_value(21)
print(L.transverse())
