import time
class TimeTrival:
    """docstring for time_this"""
    def __init__(self, num_runs=10):
        self.num_runs = num_runs
    def __call__(self, func):
        def time_counter():
            average = 0
            for i in range(self.num_runs):
                t0 = time.time()
                func()
                t1 = time.time()
                average += (t1-t0)
            average /= self.num_runs
            print('Выполнение заняло {} секунд'.format(average))
        return time_counter
    def __enter__(self):
        self.t0 = time.time()
        return self 
    def __exit__(self, *args):
        t1 = time.time()
        average = (t1-self.t0)
        print('Разность времен - {}'.format(average))
#test
def g():
    for j in range(1000000):
        pass
with TimeTrival() as t:
    g()


