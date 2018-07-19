from threading import Thread, Lock
import time


__all__ = ['ThreadPool']


class ThreadPool(object):
    def __init__(self, max_workers=10):
        if max_workers <= 0:
            raise ValueError("max_workers must be greater than 0!!!")
        self._max_workers = max_workers
        self._work_list = []
        self._work_list_lock = Lock()
        self._hasjoin = False
        self._startthread = Thread(target=self._start)

    def add(self, target, args=(), kwargs=None, highpriority=False):
        with self._work_list_lock:
            thread = Thread(target=target, args=args, kwargs=kwargs)
            if not highpriority:
                self._work_list.append(thread)
            else:
                self._work_list.insert(0, thread)

    def start(self):
        self._startthread.start()

    def _start(self):
        while True:
            current_running_workers = 0
            unruned_workers = []
            with self._work_list_lock:
                for thread in self._work_list:
                    if thread.isAlive():
                        current_running_workers += 1
                    elif not thread._started.is_set():
                        unruned_workers.append(thread)
                while current_running_workers < self._max_workers and unruned_workers:
                    thread = unruned_workers.pop(0)
                    thread.start()
                    current_running_workers += 1
            if not unruned_workers:
                break
            time.sleep(0.05)

    def join(self):
        with self._work_list_lock:
            for thread in self._work_list:
                if not thread._started.is_set():
                    time.sleep(0.5)
                if thread.is_alive():
                    thread.join()


def _main():
    def sleept(i):
        time.sleep(2)
        print("has sleep %d s..." % i)

    pool = ThreadPool(max_workers=2)
    for i in range(20):

        pool.add(target=sleept, args=(i,), highpriority=not i % 4)

    pool.start()
    pool.join()


if __name__ == '__main__':
    _main()
