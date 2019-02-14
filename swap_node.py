class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
     def __init__(self):
         self.head = None

     def push(self, data):
         new = Node(data)
         if self.head is not None:
             new.next = self.head
         self.head = new
     
     def swap(self, d1, d2):
         prev1, n1 = self._find(d1)
         prev2, n2 = self._find(d2)
         if prev1 is None:
             self.head = n2
             prev2.next = n1
         elif prev2 is None:
             self.head = n1
             prev1.next = n2
         else:
             prev1.next, prev2.next = n2, n1
         n2.next, n1.next = n1.next, n2.next
         
     def print_list(self):
         print('-'*20)
         tmp = self.head
         while tmp.next is not None:
             print(tmp.data)
             tmp = tmp.next

     def _find(self, d):
         prev = None
         tmp = self.head
         while tmp.next is not None and d != tmp.data:
             prev = tmp
             tmp = tmp.next
         return prev, tmp

def main():
    A = LinkList()
    A.push(9)
    A.push(8)
    A.push(6)
    A.push(5)
    A.push(3)
    A.push(2)
    A.push(1)
    A.print_list()
    A.swap(1, 8)
    A.print_list()
    A.swap(1, 8)
    A.print_list()
    A.swap(2, 8)
    A.print_list()
    A.swap(8, 3)
    A.print_list()

if __name__ == '__main__':
    main()
