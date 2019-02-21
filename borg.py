class Borg:
    __shared_state = {}
    
    def __init__(self):
        self.__dict__ = self.__shared_state
        self.state = 'init' 
  
    def __str__(self):
        return self.state


if __name__ == '__main__':
    a = Borg()
    b = Borg()  # a is not b
    
    print('a is b: {}'.format(a is b))  # False
    print('a.state is b.state: {}'.format(a.state is b.state))  # True

    a.state = '1'
    b.state = '2'
    print('a: {}'.format(a))
    print('b: {}'.format(b))

    a.state = '3'
    print('a: {}'.format(a))
    print('b: {}'.format(b))
    
    b.state = '4'
    print('a: {}'.format(a))
    print('b: {}'.format(b))
