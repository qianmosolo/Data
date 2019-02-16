class Node:
    def __init__(self, val):
        self.val = val
        self.p = None
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new = Node(val)
        cur = self.root
        p = None
        while cur is not None:
            p = cur
            if val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        if p is None:
            self.root = new
        else:
            if val < p.val:
                p.left = new
            else:
                p.right = new
            new.p = p

    def print_tree(self, node):
        if node:
            self.print_tree(node.left)
            print(node.val)
            self.print_tree(node.right)
 
    def pre_walk_tree(self, node):
        if node:
            print(node.val)
            self.pre_walk_tree(node.left)
            self.pre_walk_tree(node.right)

    def back_walk_tree(self, node):
        if node:
            self.back_walk_tree(node.left)
            self.back_walk_tree(node.right)
            print(node.val)
   
    def pre_walk_tree_stack(self, node):
        print('-- pre --')
        if node is None:
            return
        stack = []
        cur = node
        while cur or stack:
            while cur:
                print(cur.val),
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            cur = cur.right

    def in_walk_tree_stack(self, node):
        print('-- in --')
        if node is None:
            return
        stack = []
        cur = node
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            print(cur.val)
            cur = cur.right

    def back_walk_tree_stack(self, node):
        print('-- back --')
        if node is None:
            return
        stack1 = []
        stack2 = []
        stack1.append(node)
        while stack1:
            cur = stack1.pop()
            if cur.left:
                stack1.append(cur.left)
            if cur.right:
                stack1.append(cur.right)
            stack2.append(cur)
        while stack2:
            print(stack2.pop().val)

    def level_queue(self, node):
        if node is None:
            return
        queue = []
        queue.append(node)
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def display(self):
        self.print_tree(self.root)
        print('-'*20)

    def find(self, val):
        cur = self.root
        while cur:
            if val == cur.val:
                return cur
            elif val < cur.val:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def find_min(self, node):
        cur = node
        while cur.left:
            cur = cur.left
        return cur

    def find_max(self, node):
        cur = node
        while cur.right:
            cur = cur.right
        return cur

    def delete(self, val):
        node = self.find(val)
        if node.left is None and node.right is None:  # no sub node
            if node.p.left == node:
                node.p.left = None
            else:
                node.p.right = None
        elif node.left is None and node.right is not None:
            node.p.right = node.right
            node.right.p = node.p
        elif node.right is None and node.left is not None:
            node.p.left = node.left
            node.left.p = node.p
        else:
            tmp = self.find_min(node.right)
            if node.p is None:
                self.root = tmp
            elif node.val < node.p.val:
                node.p.left = tmp
            else:
                node.p.right = tmp
            if tmp.val < tmp.p.val:
                tmp.p.left = tmp.right
                if tmp.right:
                    tmp.right.p = tmp.p.left
            else:
                tmp.p.right = tmp.right
                if tmp.right:
                    tmp.right.p = tmp.p.right
            tmp.p = node.p
            tmp.left = node.left
            tmp.right = node.right
            
                              

def main():
    T = Tree()
    T.insert(20)
    T.insert(10)
    T.insert(30)
    T.insert(25)
    T.insert(40)
    T.insert(28)
    T.insert(27)
    T.insert(29)
    T.display()
    T.delete(27)
    T.display()
    T.level_queue(T.root)
    print('-' * 20)
    T.pre_walk_tree_stack(T.root)
    print('-' * 20)
    T.in_walk_tree_stack(T.root)
    print('-' * 20)
    T.back_walk_tree_stack(T.root)

if __name__ == '__main__':
    main()

