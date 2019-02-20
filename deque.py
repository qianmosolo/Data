class Deque:
    def __init__(self):
        self.deque = []

    def append(self, val):
        self.deque.append(val)

    def appendleft(self, val):
        self.deque.insert(0, val)

    def pop(self):
        if self.size > 0:
            return self.deque.pop()
	
    def popleft(self):
        if self.size > 0:
            return self.deque.pop(0)

    def __str__(self):
        return 'deque({})'.format(self.deque)
    
    @property
    def size(self):
        return len(self.deque)

def main():
    d = Deque()
    for i in range(3):
        d.append(i)
    for i in range(3, 6):
        d.appendleft(i)
    print(d)
    d.pop()
    print(d)
    d.popleft()
    print(d)

if __name__ == '__main__':
    main()
