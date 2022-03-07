class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None
class linkedlist:
    def __init__(self):
        self.head=None
        
    def printll(self):
        if self.head is None:
            print("Linked List is empty.\n")
        else:
            n=self.head
            print("\n")
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
            print("\n")
                
    def addbegin(self,data):
        new_node=Node(data)
        new_node.ref=self.head
        self.head=new_node
        print("\nData inserted successfully\n")
        
    def addend(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
        print("\nData inserted successfully\n")
    def add_after(self,data,x):
        n=self.head
        while n.ref is not None:
            if x==n.data:
                break
            else:
                n=n.ref
        if n is None:
            print("Node is not present in the Linked List\n")
        else:
            new_node=Node(data)
            new_node.ref=n.ref
            n.ref=new_node
            print("\nData inserted successfully\n")
            
if __name__=="__main__":
    ll1=linkedlist()
    while(True):
        key=input("\n1.Traverse the linkedlist\n2.Quit\n3.Insert a node at begin\n4.Insert after a node\n5.Insert a node at the end\n\nChoose an option: ")
        if key=='1':
            ll1.printll()
        elif key=='3':
            value=input("Enter data to the node: ")
            ll1.addbegin(value)
        elif key=='2':
            break
        elif key=='5':
            value=input("Enter data to the node: ")
            ll1.addend(value)
        elif key=='4':
            value=int(input("Enter data to the node: "))
            x=int(input("Enter the node value after which data to be inserted: "))
            ll1.add_after(value,x)
        else:
            print("Enter correct option\n")