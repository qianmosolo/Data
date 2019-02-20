class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DoubleLink:
    def __init__(self):
        self.head = None

    def push(self, val):
        new = Node(val)
        if self.head is not None:
            new.next = self.head
            self.head.prev = new
        self.head = new

    def insert(self, prev_node, val):
        if prev_node is None:
            return
        new = Node(val)
        new.next = prev_node.next
        prev_node.next = new
        new.prev = prev_node
        if new.next is not None:
            new.next.prev = new

    def append(self, val):
        new = Node(val)
        if self.head is None:
            self.head = new
            return
   
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new
        new.prev = cur
        return

    def show(self):
        cur = self.head
        while cur:
            print(cur.val, end=' ')
            cur = cur.next
        print('')

def main():
    d = DoubleLink()
    for i in range(3):
        d.push(i)
    d.show()

    for i in range(3, 6):
        d.append(i)
    d.show()

    head = d.head
    node = head.next.next
    d.insert(node, 8)
    d.show()

if __name__ == '__main__':
    main()
        
