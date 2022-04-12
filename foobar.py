import threading
from threading import Lock


class FooBar:
    def __init__(self, n):
        self.n = n
        self.LockFoo = Lock()
        self.LockBar = Lock()
        self.LockBar.acquire()


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.LockFoo.acquire()
            # printFoo() outputs "foo". Do not change or remove this line.
        	printFoo()
            self.LockBar.release()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.LockBar.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
        	printBar()
            self.LockFoo.release()