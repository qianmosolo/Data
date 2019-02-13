class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
     def __init__(self):
         self.head = None

     def insert_head(self, data):
         #new = Node(data)
         #if self.head is None:
         #    self.head = new
         #else:
         #    new.next = self.head
         #    self.head = new
         
         new = Node(data)
         if self.head is not None:
             new.next = self.head
         self.head = new

     def insert_tail(self, data):
         if self.head is None:
             self.insert_head(data)
         else:
             tmp = self.head
             while tmp.next is not None: # find the node which next pointer is None
                 tmp = tmp.next
             tmp.next =  Node(data)
      
     def delete_head(self):
         tmp = self.head
         if self.head is not None:
             self.head = tmp.next
             tmp.next = None
         return tmp

     def delete_tail(self):
         tmp = self.head
         if self.head is not None:
             if self.head.next is None:
                 self.head = None
             else:
                 while tmp.next.next is not None:
                     tmp = tmp.next
                 tmp.next = None
                 tmp = tmp.next
         return tmp
       
     def reverse(self):
         prev = None
         cur = self.head 
         while cur:
             next = cur.next
             cur.next = prev
             prev = cur
             cur = next
         self.head = prev
       
     def print_list(self):
         tmp = self.head
         print('-'*20)
         while tmp:
             print(tmp.data)
             tmp = tmp.next

     def is_empty(self):
         return self.head is None 

                       
def main():
    A = LinkedList()
    A.insert_head(1)
    A.insert_head(0)
    A.print_list()
    A.insert_tail(2)
    A.insert_tail(3)
    A.print_list()
    A.reverse()
    A.print_list()
    A.reverse()
    A.print_list()
    A.delete_head()
    A.delete_tail()
    A.print_list()

if __name__ == '__main__':
    main()
