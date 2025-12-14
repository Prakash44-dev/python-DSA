class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
ll=LinkedList()
ll.head=Node(10)
n1=Node(20)
n2=Node(30)
n3=Node(40)
n4=Node(50)
ll.head.next=n1
n1.next=n2
n2.next=n3
n3.next=n4
rev=[]
current=ll.head
while current!=None:
    print(current.data,end="->")
    rev.append(current.data)
    current=current.next
print(None)
rev.reverse() 
print(rev)


    


        
