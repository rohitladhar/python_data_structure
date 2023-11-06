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

    def sum_odd(self):
        curr = self.head
        result = 0
        index = 0
        while curr != None:
            if index % 2 == 1:
                print(curr.data)
                result = result + curr.data
            index = index + 1
            curr = curr.next
        return result
        
    def reverse(self):
        prev_node = None
        curr_node = self.head   
        while curr_node != None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
        self.head  = prev_node
       

L = Linkedlist()
L.append(13)
L.append(42)
L.append(31)
L.append(14)
L.append(20)
L.append(31)
print(L.transverse())
# L.replace_value(21)
L.reverse()
# print(L.sum_odd())
print(L.transverse())
