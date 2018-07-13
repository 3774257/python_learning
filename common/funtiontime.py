from time import time


# 装饰器用法
def getfuntime(func):
    def wrapper(*args, **kwargs):
        t1 = time()
        try:
            ret = func(*args, **kwargs)
        finally:
            print("%s running time: %s seconds." % (func.__name__, time() - t1))
        return ret
    return wrapper
