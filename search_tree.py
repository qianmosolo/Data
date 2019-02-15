class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        new = Node(data)
        if self.root is None:
            self.root = new
        else:
            cur = self.root
            while cur is not None:
                parent = cur
                if new.data < cur.data:
                    cur = cur.left
                else:
                    cur = cur.right
            if new.data < parent.data:
                parent.left = new
            else:
                parent.right = new
            new.parent = parent
         
    def delete(self, data):
        #node = Node(data)
        node = self.root
        while node is not None:
            if node.data == data:
                break
            elif node.data < data:
                node = node.left
            else:
                node = node.right
        if node is None:
            return None
        if node.left is None and node.right is None:
            if data < node.parent.data:
                node.parent.left = None
                node.parent = None
            else:
                node.parent.right = None
                node.parent = None
        elif (node.left is not None or node.right is not None):
            son = node.left or node.right
            if data < node.parent.data:
                node.parent.left = son
                son.parent = node.parent
                node.parent = None
            else:
                node.parent.right = son
                son.parent = node.parent
                node.parent = None
        else:
            tmp = self.get_max(node.left)
            self.delete(tmp.data)
            node.data = tmp.data
	     
    def get_node(self, data):
        cur = self.root
        while cur is not None and cur.data != data:
            if data < cur.data:
                cur = cur.left
            else:
                cur = cur.right
        return cur

    def get_max(self, root=None):
        if root is not None:
            cur = root
        else:
            cur = self.root
        while cur.right is not None:
            cur = cur.right
        return cur

    def display(self, cur):
        res = []
        if cur is not None:
            res.append(cur)
            res = res + self.display(cur.left)
            res = res + self.display(cur.right)
        return res
    
def main():
    T = Tree()
    T.insert(8)
    T.insert(3)
    T.insert(6)
    T.insert(1)
    T.insert(10)
    T.insert(14)
    T.insert(13)
    T.insert(4)
    T.insert(7)
    nodes = T.display(T.root)
    print([n.data for n in nodes])

if __name__ == '__main__':
    main()
