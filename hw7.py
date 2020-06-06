import time
import os
from contextlib import contextmanager


class AnotherDirectory(object):
    def __init__(self, path, exception):
        self.path = path
        self.exception = exception

    def __enter__(self):
        self.cwd = os.getcwd()
        try:
            os.chdir(os.path.expanduser(self.path))
        except self.exception as e:
            print(e)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(os.path.expanduser(self.cwd))


@contextmanager
def cd(newdir, exception):
    prevdir = os.getcwd()
    try:
        os.chdir(os.path.expanduser(newdir))
    except exception as e:
        print(e)
    try:
        yield
    finally:
        os.chdir(prevdir)



class Timer:
    def __enter__(self):
        self.start_time = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.interval = self.end_time - self.start_time
        return self.interval


def find_dublicates(my_list):
    counter = {}
    for i in my_list:
        counter[i] = counter.get(i, 0) + 1
    dublicates = {elem: count for elem, count in counter.items() if count > 1}
    return dublicates

my_list = [10, 10, 23, 10, 123, 66, 78, 123]
with Timer() as timing:
    find_dublicates(my_list)

print(timing.interval)


