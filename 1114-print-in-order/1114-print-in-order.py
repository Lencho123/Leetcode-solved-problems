from threading import Event

class Foo:
    def __init__(self):
        self.first_task = Event()
        self.second_task = Event()
        

    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        self.first_task.set()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        self.first_task.wait()
        # printSecond() outputs "second". Do not change or remove this line.
        printSecond()
        self.second_task.set()


    def third(self, printThird: 'Callable[[], None]') -> None:
        self.second_task.wait()
        # printThird() outputs "third". Do not change or remove this line.
        printThird()