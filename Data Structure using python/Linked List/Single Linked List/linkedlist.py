class node:
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
            while n is not None:
                print(n.data,"-->",end=" ")
                n=n.ref
                
    def addbegin(self,data):
        new_node=node(data)
        new_node.ref=self.head
        self.head=new_node
        print("\nData inserted successfully\n")
        
    def addend(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
            n=self.head
            while n.ref is not None:
                n=n.ref
            n.ref=new_node
            
if __name__=="__main__":
    ll1=linkedlist()
    while(True):
        key=input("\n1.Traverse the linkedlist\n2.Quit\n3.Insert a node at begin\n4.Insert a node in between\n5.Insert a node at the end\n\nChoose an option: ")
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
        else:
            print("Enter correct option\n")