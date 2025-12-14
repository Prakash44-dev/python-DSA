class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def traversal(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    def insertbegin(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def insertend(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newnode

    def deletebegin(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
        else:
            self.head = self.head.next

    def deleteend(self):
        if self.head is None:
            print("List is empty. Nothing to delete.")
        elif self.head.next is None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None


ll = Linkedlist()


ll.insertbegin(1)
ll.insertbegin(2)
ll.insertbegin(3)
print("After inserting at beginning:")
ll.traversal()


ll.insertend(4)
ll.insertend(5)
print("\nAfter inserting at end:")
ll.traversal()


ll.deletebegin()
print("\nAfter deleting at beginning:")
ll.traversal()


ll.deleteend()
print("\nAfter deleting at end:")
ll.traversal()
