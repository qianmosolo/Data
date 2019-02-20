class Stack:
    def __init__(self):
        self.stack = []

    def push(self, val):
        self.stack.append(val)
        return True

    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop()
        else:
            return ('No element')

    def show(self):
        print(self.stack)

def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(3)
    s.show()
    s.pop()
    s.pop()
    s.show()

if __name__ == '__main__':
     main()
