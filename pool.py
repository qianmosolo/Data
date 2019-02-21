class Pool(object):
    def __init__(self, queue, auto_get=False):
        self._queue = queue
        self.item = self._queue.remove() if auto_get else None

    def __enter__(self):
        if self.item is None:
            self.item = self._queue.remove()
        return self.item

    def __exit__(self, Type, value, traceback):
        if self.item is not None:
            self._queue.push(self.item)
            self.item = None
    
    def __del__(self):
        if self.item is not None:
           self._queue.push(self.item)
           self.item = None

def main():
    import queue
    
    def test_object(queue):
        pool = Pool(queue, True)
        print('in: {}'.format(pool.item))

    q = queue.Queue()
    q.push('yam')
    with Pool(q) as obj:
        print('in: {}'.format(obj))
    print('out: {}'.format(q.remove()))

    q.push('sam')
    test_object(q)
    print('out: {}'.format(q.remove()))

if __name__ == '__main__':
    main()
