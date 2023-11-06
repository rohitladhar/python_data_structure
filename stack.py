class Node:
    def __init__(self,value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.n = 0
    def isEmpty(self):
        return self.top == None
    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.n = self.n + 1
    def pop(self):
        if self.top != None:
            self.top = self.top.next
    def transverse(self):
        curr = self.top
        result = ""
        while curr != None:
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]

    def peak(self):
        if self.top != None:
            return self.top.data
        else:
            return "Stack is empty"
 
S = Stack()
S.push(1)
S.push(2)
S.push(3)
S.push(4)
print(S.transverse())
S.pop()
print(S.transverse())
print(S.peak())
