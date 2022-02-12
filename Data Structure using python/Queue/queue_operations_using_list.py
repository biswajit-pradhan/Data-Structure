class Queue:
    def enqueue(self,a,length):
        value=input("Enter a value: ")
        if len(a)==length:
            print("Queue is full\n")
        else:
            a.append(value)
            print("Successfully enqueed\n")
    def dequeue(self,a):
        if not a:
            print("Queue is empty\n")
        else:
            a.pop(0)
            print("Successfully dequeued\n")
if __name__=="__main__":
    a=[]
    i=Queue()
    while True:
        try:
            length=int(input("Enter size of queue: "))
            break
        except:
            print("\nEnter integer size only")
            #length=int(input("Enter size of queue: "))
    while(True):
        key=input("\n1.Enqueue\n2.Dequeue\n3.isEmpty\n4.isFull\n5.Traverse\n6.Quit\nChoose any option: ")
        if key=='1':
            i.enqueue(a,length)
        elif key=='2':
            i.dequeue(a)
        elif key=='3':
            if not a:
                print("True")
            else:
                print("False")
        elif key=='4':
            if len(a)==length:
                print("True")
            else:
                print("False")
        elif key=='6':
            break
        elif key=='5':
            print(a)
        else:
            print("Enter correct option\n")