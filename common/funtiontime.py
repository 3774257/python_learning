from time import time


def getfuntime(function):
    def wrapper(*args, **kwargs):
        t1 = time()
        try:
            ret = function(*args, **kwargs)
        finally:
            print("%s 运行时间：%s 秒" % (function.__name__, time() - t1))
        return ret
    return wrapper()
