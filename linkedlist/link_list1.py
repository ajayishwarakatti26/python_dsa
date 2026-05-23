# basic linked list:
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def traverse(head):
    curr=head
    while curr!=None:
       print(curr.data,end="->")
       curr=curr.next
    print("none")

def deletefrist(head):
    head=head.next
    return head


# inser at start :
def insret(head,data):
   newNode=Node(data)
   newNode.next=head
   head=newNode
   return head

# end add :
def insertAtlasat(head,data):
    curr=head
    newNode=Node(data)
    while curr.next!=None:
        curr=curr.next
   
    curr.next=newNode

    return head
    
# insert at any index:
def insrtAtindex(head,data):
    k=2
    newNode=Node(data)
    curr=head
    for i in range(k-1):
        curr=curr.next
    newNode.next=curr.next
    curr.next=newNode
    return head

def deleteend(head):
    curr=head
    while curr.next.next!=None:
        curr=curr.next
    curr.next=None
    return head

def deletatkth(head):
   
    k=1
  
    curr=head
    for i in range(k-1):
        curr=curr.next
    
    curr.next=curr.next.next
    return head


node1=Node(5)
node2=Node(6)
node3=Node(8)
node4=Node(10)

node1.next=node2
node2.next=node3
node3.next=node4

traverse(node1)


# inser at start :
# node1=insret(node1,2)
# traverse(node1)

# end :
# node1=insertAtlasat(node1,20)
# traverse(node1)

# insert at:
# node1=insrtAtindex(node1,50)
# traverse(node1)

# delet the frist:
# node1=deletefrist(node1)
# traverse(node1)

# delet at end
# node1=deleteend(node1)
# traverse(node1)

#delet at kyh:

node1=deletatkth(node1)
traverse(node1)