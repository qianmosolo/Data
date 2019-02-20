class Queue:
    def __init__(self):
        self.queue = []

    def push(self, val):
        self.queue.insert(0, val)
        return True

    def remove(self):
        if len(self.queue) > 0:
            return self.queue.pop()
    
    def show(self):
        print(self.queue)


def main():
    q = Queue()
    for i in range(10):
        q.push(i)
    q.show()
   
    for i in range(3):
        q.remove()
    q.show()


if __name__ == '__main__':
    main()
