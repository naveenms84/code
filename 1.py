class Node:
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = None
class Singlylinkedlist:
    def __init__(self):
        self.head = None
    def insertAtBeg(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def delAtBeg(self):
        if self.head == None:
            print("Singlylinkedlist is empty,can't delete")
            return
        elif self.head.next is None:
            print("Deleted node :",self.head.data)
            self.head=None
            return
        else:
            print("Deleted node :",self.head.data)
            self.head = self.head.next
            return
    def delAtEnd(self):
        if self.head == None:
            print("Singlylinkedlist is empty,can't delete")
            return
        elif self.head.next is None:
            print("Deleted node :",self.head.data)
            self.head=None
            return
        else:
            t=self.head
            while t.next.next is not None:
                t=t.next
            print("Deleted node : ", t.next.data)
            t.next=None
    def Traverse(self):
        if self.head == None:
            print("Singlylinkedlist is empty,can't display")
            return
        current=self.head
        print("List items")
        while (current ):
            print(current.data)
            current=current.next
    def Search(self,num):
        if self.head == None:
            print("Singlylinkedlist is empty,can't search")
            return
        current=self.head
        loc=1
        while (current):
            if current.data == num:
                print("Seraching is successful ,Found at location : ",loc)
                return
            loc=loc+1
            current=current.next
Sll=Singlylinkedlist()
Sll.Traverse()
Sll.delAtBeg()
Sll.delAtEnd()
Sll.Search(5)
Sll.insertAtBeg(10)
Sll.insertAtBeg(20)
Sll.insertAtBeg(30)
Sll.insertAtBeg(40)
Sll.insertAtBeg(50)
Sll.Traverse()
Sll.Search(10)
Sll.delAtBeg()
Sll.delAtEnd()
Sll.Traverse()
