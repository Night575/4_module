import time


class CodeTimer:
    def __init__(self):
        self.start = None

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print(exc_type)
        # print(exc_tb)
        # print(exc_val)
        t = time.time() - self.start
        print('Итого время работы составило', t, 'сек')
        return True

timer = CodeTimer()

with timer:
    l = [i for i in range(100)]
    l[101]
    5 + 'a'
