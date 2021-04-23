from threading import Thread


def func1(soma):

    for i in range(20000000):
        soma += i*0.4
    print(f'soma1: {soma}')


def func2():
    soma = 3

    for i in range(2000000):
        soma += i*0.2
    print(f'soma2: {soma}')


# func1()
# func2()

if __name__ == '__main__':

    a = Thread(target=func1(10)).start()
    Thread(target=func2).start()


class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)

    def dequeue(self, data):
        data = None
        try:
            data = self.queue.pop(0)
        catch IndexError as ex:
            pass

        return data

    def is_empty(self):
        return len(self.queue) == 0


def foo(bar):
    print('dani {bar}')

    return 'foo'


q = Queue()
t = Thread(target=lambda q, arg: q.enqueue(foo(arg)), args=(q, 'world!'))
t.start()
t.join()
result = que.get()
print(result)
