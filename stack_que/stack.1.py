class Stack:
  def __init__(self):
    self.stack = []

  def push(self, element):
    self.stack.append(element)

  def pop(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack.pop()

  def peek(self):
    if self.isEmpty():
      return "Stack is empty"
    return self.stack[-1]

  def isEmpty(self):
    return len(self.stack) == 0

  def size(self):
    return len(self.stack)

# Create a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

# print("Stack: ", myStack.stack)
# print("Pop: ", myStack.pop())
# print("Stack after Pop: ", myStack.stack)
# print("Peek: ", myStack.peek())
# print("isEmpty: ", myStack.isEmpty())
# print("Size: ", myStack.size())


# linked list :
class Node:
   def __init__(self,data):
      self.data=data
      self.next=None
     

class Stack:
  def __init__(self):
     self.top=None
     self.len=0

  def push(self,x):
     self.len+=1
   
     if self.top is None:
       self.top=Node(x)
       return
     else:
       newnode=Node(x)
       newnode.next=self.top
       self.top=newnode

  def pop(self):
     
     if self.top is None:
       return-1
     
     self.len -=1
     x= self.top.data
     self.top=self.top.next
     return x
   
  def gettop(self):
     if self.top is None:
       return-1
     return self.top.data 
  
  def size(self):
    return self.len
 

s=Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)

print(s.size())
print(s.pop())
print(s.gettop())

    


 



  
   
