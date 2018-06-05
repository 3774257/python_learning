from common.funtiontime import getfuntime
import random


def bubble_sort(li):
    n = len(li)
    for i in range(n - 1):
        for j in range(i+1, n-i-1):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]



if __name__ == '__main__':
    l = list(range(10))
    random.shuffle(l)
    print(l)
    bubble_sort(l)
    print(l)