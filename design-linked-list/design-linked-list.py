class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
        
class MyLinkedList:

    def __init__(self):
        self.head=None

    def get(self, index: int) -> int:
        if self.head==None:
            return -1
        i=0
        curr=self.head
        while(i<index and curr!=None):
            curr=curr.next
            i=i+1
        if curr==None:
            return -1
        else:
            return curr.val
        # if self.head==None:
        #     return -1
        # i=0
        # prev=self.head
        # after=self.head.next
        # while(i<index and after.next!=None):
        #     prev=after
        #     after=after.next
        #     i=i+1
        # return after.val

    def addAtHead(self, val: int) -> None:
        newNode=Node(val)
        newNode.next=self.head
        self.head=newNode

    def addAtTail(self, val: int) -> None:
        newNode=Node(val)
        curr=self.head
        if self.head!=None:
            after=self.head.next
            while(after!=None):
                curr=after
                after=after.next
            curr.next=newNode
        elif self.head==None:
            self.head=newNode
            self.head.next=None
            
            
    def addAtIndex(self, index: int, val: int) -> None:          
        i=0
        newNode=Node(val)
        prev=self.head
        if (self.head==None and index>0):
            return
        elif (self.head==None) and index==0:
            self.head=newNode
        elif self.head!=None and index==0:
            newNode.next=self.head
            self.head=newNode
        else:
            after=self.head.next

            while(i<index-1):
                if after==None:
                    return 
                # print("value of prev", prev.val, "valueof",after)

                prev=after
                after=after.next
                i=i+1
            # print("Added at index ", i)
            # print("after value is", after)
            newNode.next=after
            prev.next=newNode
            # print("value of prev", prev.val, "value added",prev.next.val,"valueof",after)

        
    def deleteAtIndex(self, index: int) -> None:
        # pass
        i=0
        prev=self.head
        after=self.head.next
        
        if index==0:
            self.head=after
        else:
            while(i<index-1):
                if after==None:
                    return 
                prev=after
                after=after.next
                i=i+1
            if after!=None:
                prev.next=after.next
            else:
                prev.next=None


#Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)