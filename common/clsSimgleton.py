
# 单例模式


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance


if __name__ == '__main__':
    class MyClass(Singleton):
        def __init__(self, name=None):
            if name:
                self.name = name

    a = MyClass()
    b = MyClass()
    print(a, b)
