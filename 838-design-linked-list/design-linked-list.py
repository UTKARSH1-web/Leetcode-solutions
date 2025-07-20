class MyLinkedList:

    def __init__(self):
        self.l=[]

    def get(self, index: int) -> int:
        # print(self.l)
        if len(self.l)>index:
            return self.l[index]
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        self.l.insert(0,val)

    def addAtTail(self, val: int) -> None:
        self.l.append(val)
        # print(self.l)

    def addAtIndex(self, index: int, val: int) -> None:
        if len(self.l)>=index:
            self.l.insert(index,val)
        # print(self.l)

    def deleteAtIndex(self, index: int) -> None:
        if len(self.l)>=index+1:
            self.l.pop(index)
        # print(self.l)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)