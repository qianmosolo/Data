class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insertHead(self, data):
        new = Node(data)
        if self.head is None:
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
        self.head = new

    def insertTail(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

    def deleteHead(self):
        self.head = self.head.next
        self.head.prev = None

    def deleteTail(self):
        self.tail = self.tail.prev
        self.tail.next = None
        
    def delete(self, x):
        cur = self.head
        while cur.data != x:
            cur = cur.next
        
        if cur == self.head:
            self.deleteHead()
        elif cur == self.tail:
            self.deleteTail()
        else:
            cur.prev.next = cur.next
            cur.next.prev = cur.prev

    def print_list(self):
        print('-'*20)
        tmp = self.head
        while tmp:
            print(tmp.data)
            tmp = tmp.next

def main():
    A = LinkList()
    A.insertHead(8)
    A.insertTail(9)
    A.insertHead(7)
    A.insertHead(6)
    A.insertHead(5)
    A.print_list()
    A.delete(5)
    A.print_list()
    A.delete(9)
    A.print_list()
    A.delete(7)
    A.print_list()

if __name__ == '__main__':
    main()
