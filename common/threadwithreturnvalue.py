import threading


"""带返回值的线程库"""
class ThreadWithReturnValue(threading.Thread):

    def __init__(self, target=None, args=(), kwargs=None):
        super(ThreadWithReturnValue, self).__init__()
        if kwargs is None:
            kwargs = {}
        self._target = target
        self._args = args
        self._kwargs = kwargs
        self._result = None

    def run(self):
        try:
            if self._target:
                self._result = self._target(*self._args, **self._kwargs)
        finally:
            # Avoid a refcycle if the thread is running a function with
            # an argument that has a member that points to the thread.
            del self._target, self._args, self._kwargs

    def get_return(self):
        try:
            return self._result
        except Exception:
            return None


if __name__ == '__main__':
    import time

    def foo(a, b, c=2):
        time.sleep(1)
        return a, b*2, c*3

    t1 = time.time()
    li = []
    for i in range(5):
        t = ThreadWithReturnValue(target=foo, args=(i, i+1,), kwargs={'c': i+2})
        li.append(t)
        t.start()

    for t in li:
        t.join()
        print(t.get_return())

    print("Cost Time: %.4f" % (time.time()-t1))
